import csv
from data_handlers import filter_scans, find_worker
from list_utils import group_into_pairs

def write_to_csv(worker_name, regs_groups):
  with open(worker_name.replace(" ", "_") + '_report.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')

    writer.writerow([
      'Enter Terminal',
      'Enter Card',
      'Enter Time',
      'Exit Terminal',
      'Exit Card',
      'Exit Time'
    ])

    for reg_group in regs_groups:
      enter_reg = reg_group[0]
      row = [
        enter_reg['terminal_id'],
        enter_reg['card_id'],
        enter_reg['time']
      ]

      if len(reg_group) == 2:
        exit_reg = reg_group[1]

        row = row + [
          exit_reg['terminal_id'],
          exit_reg['card_id'],
          exit_reg['time']
        ]
      
      writer.writerow(row)

def generate_report(person_id):
  global scans

  worker = find_worker('id', person_id)
  if worker is None:
    raise "Worker is not registered in the system"

  scans = filter_scans(lambda r: r.get('person_id') == person_id)
  sorted_regs = sorted(scans, key=lambda r: r['time'])
  regs_groups = group_into_pairs(sorted_regs)

  write_to_csv(worker['full_name'], regs_groups)
