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

'impact': {
  'currentlyInfected': 0,
  'infectionsByRequestedTime': 0,
  'severeCasesByRequestedTime': 0,
  'hospitalBedsByRequestedTime': 0,
  'casesForICUByRequestedTime': 0,
  'casesForVentilatorsByRequestedTime': 0,
  'dollarsInFlight': 0
  },
'severeImpact': {
  'currentlyInfected': 0,
  'infectionsByRequestedTime': 0,
  'severeCasesByRequestedTime': 0,
  'hospitalBedsByRequestedTime': 0,
  'casesForICUByRequestedTime': 0,
  'casesForVentilatorsByRequestedTime': 0,
  'dollarsInFlight': 0
  },
}


# Challenge 1 
def currently__Infected(currently_Infected, val):
   
    currentlyInfected = currently_Infected * val
      

    return currentlyInfected

def infectionsByRequestedTime(time, x, currentlyInfected):
  
  if time == 'days':        
    iBRT = math.floor(currentlyInfected * (2**(x//3)))
  elif time == 'months':
    iBRT = math.floor(currentlyInfected * (2**((x*30)//3)))
  elif time == 'weeks':
    iBRT = math.floor(currentlyInfected * (2**((x*7)//3)))
  

  return iBRT

# Challenge 2

def severeCasesByRequestedTime(iBRT):
    sCBRT = math.floor((iBRT * 0.15))
    
    return sCBRT
def hospitalBedSpaceByRequestedTime(tHB,sCBRT):

    hBS = math.floor((tHB * 0.35))
    hBSBRT = hBS - sCBRT

    return hBSBRT

# Challenge 3

def casesForICUByRequestedTime(iBRT):
    c4ICU = math.floor((iBRT * 0.05))
    return c4ICU

def casesForVentilatorsByRequestedTime(iBRT):
    c4Vent = math.floor((iBRT * 0.02))

    return c4Vent

def dollarsInFlight(iBRT, pop,t2E, dI):
    dIF = (iBRT * pop * dI)/t2E

    return math.floor((dIF))


def estimator(data):
    
    currentlyInfected = values['impact']['currentlyInfected'] = currently__Infected(data['reportedCases'], 10)

    iBRT = values['impact']['infectionsByRequestedTime'] = infectionsByRequestedTime(data['periodType'], data['timeToElapse'], currentlyInfected)
    
    sCBRT = values['impact']['severeCasesByRequestedTime'] = severeCasesByRequestedTime(iBRT)
    
    values['impact']['hospitalBedsByRequestedTime'] = hospitalBedSpaceByRequestedTime(data['totalHospitalBeds'], sCBRT)
    
    values['impact']['casesForICUByRequestedTime'] = casesForICUByRequestedTime(iBRT)
    values['impact']['casesForVentilatorsByRequestedTime'] = casesForVentilatorsByRequestedTime(iBRT)
    values['impact']['dollarsInFlight'] = dollarsInFlight(iBRT, data['region']['avgDailyIncomePopulation'], data['timeToElapse'], data['region']['avgDailyIncomeInUSD'])

    
    currentlyInfected = values['severeImpact']['currentlyInfected'] = currently__Infected(data['reportedCases'], 50)
    iBRT = values['severeImpact']['infectionsByRequestedTime'] = infectionsByRequestedTime(data['periodType'], data['timeToElapse'], currentlyInfected)    
    sCBRT = values['severeImpact']['severeCasesByRequestedTime'] = severeCasesByRequestedTime(iBRT)
    
    values['severeImpact']['hospitalBedsByRequestedTime'] = hospitalBedSpaceByRequestedTime(data['totalHospitalBeds'], sCBRT)
    
    values['severeImpact']['casesForICUByRequestedTime'] = casesForICUByRequestedTime(iBRT)
    values['severeImpact']['casesForVentilatorsByRequestedTime'] = casesForVentilatorsByRequestedTime(iBRT)
    values['severeImpact']['dollarsInFlight'] = dollarsInFlight(iBRT, data['region']['avgDailyIncomePopulation'], data['timeToElapse'], data['region']['avgDailyIncomeInUSD'])
    dt = data
    data = {}
    
    data['data'] = {}
    data['data'] =dt
    data.update(values)

       
    return data

#estimator(data)
