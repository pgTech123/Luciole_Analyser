def debug_line_to_dict(debug_info):
    # Timestamp,VOLTAGE_GLOBAL,TEMPERATURE_CELL1,TEMPERATURE_CELL2,TEMPERATURE_CELL3,
    # TEMPERATURE_CELL4,CURRENT_CELL1,CURRENT_CELL2,CURRENT_CELL3,CURRENT_CELL4,
    # TEMPERATURE_LASER1,TEMPERATURE_LASER2,TEMPERATURE_LASER3,TEMPERATURE_LASER4,
    # BAT_CELL1,BAT_CELL2,BAT_CELL3,BAT_TOT,BAT_CURRENT,BAT_TEMPERATURE,BAT_CELL_BALANCING,BAT_LEVEL,
    # POWER_SUPPLY_VOLTAGE,POWER_SUPPLY_CURRENT
    items = debug_info[:-1].split(',')  # Remove '\n'
    if len(items) < 21:
        return None
    dictionary = {'timestamp': items[0],
                  'voltage_global': items[1],
                  'temperature_cell1': items[2],
                  'temperature_cell2': items[3],
                  'temperature_cell3': items[4],
                  'temperature_cell4': items[5],
                  'current_cell1': items[6],
                  'current_cell2': items[7],
                  'current_cell3': items[8],
                  'current_cell4': items[9],
                  'temperature_laser1': items[10],
                  'temperature_laser2': items[11],
                  'temperature_laser3': items[12],
                  'temperature_laser4': items[13],
                  'battery_cell1': items[14],
                  'battery_cell2': items[15],
                  'battery_cell3': items[16],
                  'battery_total': items[17],
                  'battery_current': items[18],
                  'battery_temperature': items[19],
                  'battery_balancing': items[20],
                  'battery_level': items[21],
                  'power_supply_voltage': items[22],
                  'power_supply_current': items[23]}
    return dictionary
