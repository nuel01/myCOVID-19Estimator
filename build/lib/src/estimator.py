# by adegunlehinabayomi@gmail.com
# ______COVID-19 Impact Estimator_______



reportedCases = data_reported_cases
population = data-population
timeToElapse = data-time-to-elapse
totalHospitalBeds = data-total-hospital-beds


c_i = 0
iBRT = 0

    #return reportedCases, population, timeToElapse, totalHospitalBeds



# Challenge 1 
def currentlyInfected(r_c, check):
    if check == 'impact':
      impactCurrentlyInfected = reportedCases * 10
      c_i = impactCurrentlyInfected

      return c_i

    elif check == 'severe':
      severeImpactCurrentlyInfected = reportedCases * 50
      c_i = severeImpactCurrentlyInfected

      return c_i

def infectionByRequiredTime(time, x):
   
    if time == 'days':
        infectionByRequiredTime = ((c_i * 512)/28) * timeToElapse
    elif time == 'months':
        infectionByRequiredTime = ((c_i * 512)/28) * 30 * timeToElapse
    elif time == 'weeks':
        infectionByRequiredTime = ((c_i * 512)/28) * 7 * timeToElapse

    return infectionByRequiredTime

    # elif check == 'severe':
    #     if time = days:
    #       infectionByRequiredTime = ((c_i * 512)/28) * x
    #   elif time = 'months':
    #       infectionByRequiredTime = ((c_i * 512)/28) * 30 * x
    #   elif time = 'weeks':
    #       infectionByRequiredTime = ((c_i * 512)/28) * 7 * x

# Challenge 2

def severeCasesByRequiredTime():
    iBRT = c_i * 512 * 0.15

    return iBRT
def hospitalBedSpaceByRequiredTime():

    hBS = hospitalBedSpace * 0.35
    hBSBRT = hBS - iBRT

    return print(hBSBRT,' Hospital Bedspaces are available')

# Challenge 3

def casesForICUByRequestedTime():
    c4ICU = iBRT * 0.05
    return c4ICU

def casesForVentilatorsByRequestedTime():
    c4Vent = iBRT * 0.02

    return c4Vent

def dollarsInFlight():
    dIF = iBRT * 30

    return dIF


def impactCase(r_c, time):
    i = 'impact'
    currentlyInfected(reportedCases, i)
    infectionByRequiredTime(time, i)


def severeImpact():
    s = 'severe'
    currentlyInfected(reportedCases, s)
    infectionByRequiredTime(time, s)


def estimator(data):

    data_supplied = data
    impactCase()
    severeImpact()

    return data, severeImpact, impactCase

estimator()
