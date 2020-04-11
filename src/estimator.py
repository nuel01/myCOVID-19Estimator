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

# Challenge 1 
def currently__Infected(currently_Infected, val):
   
    currentlyInfected = currently_Infected * val
      

    return currentlyInfected

def infectionByRequiredTime(time, x, currentlyInfected):
  
  if time == 'days':        
    iBRT = currentlyInfected * (2**(x//3))
  elif time == 'months':
    iBRT = currentlyInfected * (2**((x*30)//3))
  elif time == 'weeks':
    iBRT = currentlyInfected * (2**((x*7)//3))
  

  return iBRT

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
    dIF = (iBRT * pop * dI)/t2E

    return round(dIF)


def estimator(data):
    
    currentlyInfected = values['estimate']['impact']['currentlyInfected'] = currently__Infected(data['reportedCases'], 10)

    iBRT = values['estimate']['impact']['infectionByRequiredTime'] = infectionByRequiredTime(data['periodType'], data['timeToElapse'], currentlyInfected)
    
    sCBRT = values['estimate']['impact']['severeCasesByRequiredTime'] = severeCasesByRequiredTime(iBRT)
    
    values['estimate']['impact']['totalHospitalBeds'] = hospitalBedSpaceByRequiredTime(data['totalHospitalBeds'], sCBRT)
    
    values['estimate']['impact']['casesForICUByRequestedTime'] = casesForICUByRequestedTime(iBRT)
    values['estimate']['impact']['casesForVentilatorsByRequestedTime'] = casesForVentilatorsByRequestedTime(iBRT)
    values['estimate']['impact']['dollarsInFlight'] = dollarsInFlight(iBRT, data['region']['avgDailyIncomePopulation'], data['timeToElapse'], data['region']['avgDailyIncomeInUSD'])

    
    currentlyInfected = values['estimate']['severeImpact']['currentlyInfected'] = currently__Infected(data['reportedCases'], 50)
    iBRT = values['estimate']['severeImpact']['infectionByRequiredTime'] = infectionByRequiredTime(data['periodType'], data['timeToElapse'], currentlyInfected)    
    sCBRT = values['estimate']['severeImpact']['severeCasesByRequiredTime'] = severeCasesByRequiredTime(iBRT)
    
    values['estimate']['severeImpact']['totalHospitalBeds'] = hospitalBedSpaceByRequiredTime(data['totalHospitalBeds'], sCBRT)
    
    values['estimate']['severeImpact']['casesForICUByRequestedTime'] = casesForICUByRequestedTime(iBRT)
    values['estimate']['severeImpact']['casesForVentilatorsByRequestedTime'] = casesForVentilatorsByRequestedTime(iBRT)
    values['estimate']['severeImpact']['dollarsInFlight'] = dollarsInFlight(iBRT, data['region']['avgDailyIncomePopulation'], data['timeToElapse'], data['region']['avgDailyIncomeInUSD'])
    data.update(values)

    
    return data

#estimator(data)
