return_value = True
def check_tempearture(temperature):
  global return_value
  if temperature < 0 or temperature > 45:
    print('Temperature is out of range!')
    return_value = False
  else:
    return_value = True


def validate_soc(soc):
    if soc < 20 or soc > 80:
        print('State of Charge is out of range!')
        return False
    else:
        return True
    
def check_soc(soc):
   global return_value
   if return_value is True:
     return_value = validate_soc(soc)

def check_charge_rate(charge_rate):
  global return_value
  if return_value is True:
      if charge_rate > 0.8:
        print('Charge rate is out of range!')
        return_value = False

def battery_is_ok(temperature, soc, charge_rate):

    check_tempearture(temperature)
    check_soc(soc)
    check_charge_rate(charge_rate)
    return return_value


if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
