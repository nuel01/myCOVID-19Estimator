# by adegunlehinabayomi@gmail.com
# ______COVID-19 Impact Estimator_______
import math
'''
data ={
'data' : {
 'region': {
 'name': "Africa",
 'avgAge': 19.7,
 'avgDailyIncomeInUSD': 4,
 'avgDailyIncomePopulation': 0.73
 },
 'periodType': "days",
 'timeToElapse': 38,
 'reportedCases': 2747,
 'population': 92931687,
 'totalHospitalBeds': 678874
}
}
'''
values = {
'estimate' : {
'impact': {
  'currentlyInfected': 0,
  'infectionByRequiredTime': 0,
  'severeCasesByRequiredTime': 0,
  'totalHospitalBeds': 0,
  'casesForICUByRequestedTime': 0,
  'casesForVentilatorsByRequestedTime': 0,
  'dollarsInFlight': 0
  },
'severeImpact': {
  'currentlyInfected': 0,
  'infectionByRequiredTime': 0,
  'severeCasesByRequiredTime': 0,
  'totalHospitalBeds': 0,
  'casesForICUByRequestedTime': 0,
  'casesForVentilatorsByRequestedTime': 0,
  'dollarsInFlight': 0
  },
}
}
# reportedCases = data_reported_cases
# population = data-population
# timeToElapse = data-time-to-elapse
# totalHospitalBeds = data-total-hospital-beds




    #return reportedCases, population, timeToElapse, totalHospitalBeds



# Challenge 1 
def currentlyInfected(currentlyInfected, val):
    #if check == 'impact':
    c_i = currentlyInfected * val
        #data['estimate']['impact']['currentlyInfected']  = impactCurrentlyInfected

    return c_i

    # elif check == 'severe':
    #     c_i = severeImpactCurrentlyInfected = r_c * 50
    #     #data['estimate']['severeImpact']['currentlyInfected']  = severeImpactCurrentlyInfected

    #     return c_i

def infectionByRequiredTime(time, x, c_i):
  #if check == 'impact':
  if time == 'days':        
    iBRT = c_i * (2**(x//3))
  elif time == 'months':
    iBRT = c_i * (2**((x*30)//3))
  elif time == 'weeks':
    iBRT = c_i * (2**((x*7)//3))
   # data['estimate']['impact']['infectionByRequiredTime'] = iBRT

  return iBRT

  # elif check == 'severe':
  #   if time == 'days':        
  #     iBRT = c_i * (2**(x//3))
  #   elif time == 'months':
  #     iBRT = c_i * (2**((x*30)//3))
  #   elif time == 'weeks':
  #     iBRT = c_i * (2**((x*7)//3))
  #   data['estimate']['severeImpact']['infectionByRequiredTime'] = iBRT
  #   return iBRT

# Challenge 2

def severeCasesByRequiredTime(iBRT):
    sCBRT = round(iBRT * 0.15)
    
    return sCBRT
def hospitalBedSpaceByRequiredTime(tHB,sCBRT):

    hBS = round(tHB * 0.35)
    hBSBRT = hBS - sCBRT

    return hBSBRT

# Challenge 3

def casesForICUByRequestedTime(iBRT):
    c4ICU = round(iBRT * 0.05)
    return c4ICU

def casesForVentilatorsByRequestedTime(iBRT):
    c4Vent = round(iBRT * 0.02)

    return c4Vent

def dollarsInFlight(iBRT, pop,t2E, dI):
    dIF = (iBRT * pop * dI)*t2E

    return round(dIF)

'''
def impactCase(r_c, time, t2E, tHB, pop, dI):
    i = 'impact'
    c_i = currentlyInfected(r_c, i)
    iBRT = infectionByRequiredTime(time, i, t2E, c_i)
    
    sCBRT = data['estimate']['impact']['severeCasesByRequiredTime'] = severeCasesByRequiredTime(iBRT)
    
    data['estimate']['impact']['totalHospitalBeds'] = hospitalBedSpaceByRequiredTime(tHB, sCBRT)
    
    data['estimate']['impact']['casesForICUByRequestedTime'] = casesForICUByRequestedTime(iBRT)
    data['estimate']['impact']['casesForVentilatorsByRequestedTime'] = casesForVentilatorsByRequestedTime(iBRT)
    data['estimate']['impact']['dollarsInFlight'] = dollarsInFlight(iBRT, pop, t2E, dI)


def severeImpact(r_c, time, t2E, tHB, pop, dI):
    s = 'severe'
    c_i = currentlyInfected(r_c, s)
    iBRT = infectionByRequiredTime(time, s, t2E, c_i)    
    sCBRT = data['estimate']['severeImpact']['severeCasesByRequiredTime'] = severeCasesByRequiredTime(iBRT)
    
    data['estimate']['severeImpact']['totalHospitalBeds'] = hospitalBedSpaceByRequiredTime(tHB, sCBRT)
    
    data['estimate']['severeImpact']['casesForICUByRequestedTime'] = casesForICUByRequestedTime(iBRT)
    data['estimate']['severeImpact']['casesForVentilatorsByRequestedTime'] = casesForVentilatorsByRequestedTime(iBRT)
    data['estimate']['severeImpact']['dollarsInFlight'] = dollarsInFlight(iBRT, pop, t2E, dI)

'''
def estimator(data):
    
    c_i = values['estimate']['impact']['currentlyInfected'] = currentlyInfected(data['data']['reportedCases'], 10)

    iBRT = values['estimate']['impact']['infectionByRequiredTime'] = infectionByRequiredTime(data['data']['periodType'], data['data']['timeToElapse'], c_i)
    
    sCBRT = values['estimate']['impact']['severeCasesByRequiredTime'] = severeCasesByRequiredTime(iBRT)
    
    values['estimate']['impact']['totalHospitalBeds'] = hospitalBedSpaceByRequiredTime(data['data']['totalHospitalBeds'], sCBRT)
    
    values['estimate']['impact']['casesForICUByRequestedTime'] = casesForICUByRequestedTime(iBRT)
    values['estimate']['impact']['casesForVentilatorsByRequestedTime'] = casesForVentilatorsByRequestedTime(iBRT)
    values['estimate']['impact']['dollarsInFlight'] = dollarsInFlight(iBRT, data['data']['region']['avgDailyIncomePopulation'], data['data']['timeToElapse'], data['data']['region']['avgDailyIncomeInUSD'])

    
    c_i = values['estimate']['severeImpact']['currentlyInfected'] = currentlyInfected(data['data']['reportedCases'], 50)
    iBRT = values['estimate']['severeImpact']['infectionByRequiredTime'] = infectionByRequiredTime(data['data']['periodType'], data['data']['timeToElapse'], c_i)    
    sCBRT = values['estimate']['severeImpact']['severeCasesByRequiredTime'] = severeCasesByRequiredTime(iBRT)
    
    values['estimate']['severeImpact']['totalHospitalBeds'] = hospitalBedSpaceByRequiredTime(data['data']['totalHospitalBeds'], sCBRT)
    
    values['estimate']['severeImpact']['casesForICUByRequestedTime'] = casesForICUByRequestedTime(iBRT)
    values['estimate']['severeImpact']['casesForVentilatorsByRequestedTime'] = casesForVentilatorsByRequestedTime(iBRT)
    values['estimate']['severeImpact']['dollarsInFlight'] = dollarsInFlight(iBRT, data['data']['region']['avgDailyIncomePopulation'], data['data']['timeToElapse'], data['data']['region']['avgDailyIncomeInUSD'])
    data.update(values)

    #data_supplied = data
    # impactCase(data['data']['reportedCases'],data['data']['periodType'], data['data']['timeToElapse'], data['data']['totalHospitalBeds'], data['data']['region']['avgDailyIncomePopulation'],data['data']['region']['avgDailyIncomeInUSD'])
    
    # severeImpact(data['data']['reportedCases'],data['data']['periodType'], data['data']['timeToElapse'], data['data']['totalHospitalBeds'],data['data']['region']['avgDailyIncomePopulation'],data['data']['region']['avgDailyIncomeInUSD'])

    return data

#estimator(data)
