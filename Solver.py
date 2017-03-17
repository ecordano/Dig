# Import PuLP modeler functions
from pulp import *
#import cgi

#formData = cgi.FieldStorage()

def solve(time, land1, land2, land3):
    # Creates a list of the produce options
    crops = ['CUC', 'EGG', 'STOM', 'GBEAN', 'BSQ', 'CTOM', 'ZUC', 'WAT', 'BPEP', 'STR', 'POT', 'SCORN', 'CAR', 'BEET',
             'ONS', 'RAD', 'SPEA', 'LET', 'GAR', 'BSPR', 'KALE', 'SPCH']

    # A dictionary of the costs of each of the crops
    # costs = {'CUC': ,
    #          'EGG': ,
    #          'STOM': ,
    #          'GBEAN': ,
    #          'BSQ': ,
    #          'CTOM': ,
    #          'ZUC': ,
    #          'WAT': ,
    #          'BPEP': ,
    #          'STR': ,
    #          'POT': ,
    #          'SCORN': ,
    #          'CAR': ,
    #          'BEET': ,
    #          'ONS': ,
    #          'RAD': ,
    #          'SPEA': ,
    #          'LET': ,
    #          'GAR': ,
    #          'BSPR': ,
    #          'KALE': ,
    #          'SPCH': }

    # A dictionary of the land for each of the crops
    land = {'CUC': 1.0, 'EGG': 1.0, 'STOM': 4.0, 'GBEAN': 0.1, 'BSQ': 1.0, 'CTOM': 1.0, 'ZUC': 1.0, 'WAT': 2.0,
            'BPEP': 1.0,
            'STR': 0.3, 'POT': 1.0, 'SCORN': 1.0, 'CAR': 0.1, 'BEET': 0.1, 'ONS': 0.1, 'RAD': 0.1, 'SPEA': 1.0,
            'LET': 0.3,
            'GAR': 0.1, 'BSPR': 2.3, 'KALE': 1.0, 'SPCH': 0.1}

    # A dictionary of the land where sunlight level is [1,2,3]
    landSun1 = {'CUC': LpStatusInfeasible, 'EGG': LpStatusInfeasible, 'STOM': LpStatusInfeasible,
                'GBEAN': LpStatusInfeasible, 'BSQ': LpStatusInfeasible, 'CTOM': LpStatusInfeasible,
                'ZUC': LpStatusInfeasible, 'WAT': LpStatusInfeasible, 'BPEP': LpStatusInfeasible,
                'STR': LpStatusInfeasible,
                'POT': LpStatusInfeasible, 'SCORN': LpStatusInfeasible, 'CAR': LpStatusInfeasible,
                'BEET': LpStatusInfeasible, 'ONS': LpStatusInfeasible, 'RAD': LpStatusInfeasible,
                'SPEA': LpStatusInfeasible, 'LET': 0.3, 'GAR': 0.1, 'BSPR': 2.3, 'KALE': 1.0, 'SPCH': 0.1}

    # A dictionary of the land where sunlight level is [1,2,3]
    landSun2 = {'CUC': LpStatusUndefined, 'EGG': LpStatusUndefined, 'STOM': LpStatusUndefined,
                'GBEAN': LpStatusUndefined,
                'BSQ': LpStatusUndefined, 'CTOM': LpStatusUndefined, 'ZUC': LpStatusUndefined, 'WAT': LpStatusUndefined,
                'BPEP': 1.0, 'STR': 0.3, 'POT': 1.0, 'SCORN': 1.0, 'CAR': 0.1, 'BEET': 0.1, 'ONS': 0.1, 'RAD': 0.1,
                'SPEA': 1.0, 'LET': LpStatusUndefined, 'GAR': LpStatusUndefined, 'BSPR': LpStatusUndefined,
                'KALE': LpStatusUndefined, 'SPCH': LpStatusUndefined}

    # A dictionary of the land where sunlight level is [1,2,3]
    landSun3 = {'CUC': 1.0, 'EGG': 1.0, 'STOM': 4.0, 'GBEAN': 0.1, 'BSQ': 1.0, 'CTOM': 1.0, 'ZUC': 1.0, 'WAT': 2.0,
                'BPEP': LpStatusUndefined, 'STR': LpStatusUndefined, 'POT': LpStatusUndefined,
                'SCORN': LpStatusUndefined,
                'CAR': LpStatusUndefined, 'BEET': LpStatusUndefined, 'ONS': LpStatusUndefined, 'RAD': LpStatusUndefined,
                'SPEA': LpStatusUndefined, 'LET': LpStatusUndefined, 'GAR': LpStatusUndefined,
                'BSPR': LpStatusUndefined,
                'KALE': LpStatusUndefined, 'SPCH': LpStatusUndefined}

    # A dictionary of the sunlight req of each of the crops
    sunlight = {'CUC': 3, 'EGG': 3, 'STOM': 3, 'GBEAN': 3, 'BSQ': 3, 'CTOM': 3, 'ZUC': 3, 'WAT': 3, 'BPEP': [2, 3],
                'STR': [2, 3], 'POT': [2, 3], 'SCORN': [2, 3], 'CAR': [2, 3], 'BEET': [2, 3], 'ONS': [2, 3],
                'RAD': [2, 3],
                'SPEA': [2, 3], 'LET': [1, 2, 3], 'GAR': [1, 2, 3], 'BSPR': [1, 2, 3], 'KALE': [1, 2, 3],
                'SPCH': [1, 2, 3]}

    # A dictionary of the expected maintenance time of each of the crops
    maintenance = {'CUC': 0.001574074, 'EGG': 0.004722222, 'STOM': 0.003148148, 'GBEAN': 0.001574074,
                   'BSQ': 0.003148148,
                   'CTOM': 0.001574074, 'ZUC': 0.003148148, 'WAT': 0.004722222, 'BPEP': 0.003148148, 'STR': 0.003148148,
                   'POT': 0.001574074, 'SCORN': 0.003148148, 'CAR': 0.003148148, 'BEET': 0.001574074,
                   'ONS': 0.001574074,
                   'RAD': 0.001574074, 'SPEA': 0.001574074, 'LET': 0.001574074, 'GAR': 0.001574074, 'BSPR': 0.004722222,
                   'KALE': 0.003148148, 'SPCH': 0.001574074}

    # A dictionary of the potential selling prices of each of the crops
    price = {'CUC': 1.49, 'EGG': 1.49, 'STOM': 1.69, 'GBEAN': 3.52, 'BSQ': 0.79, 'CTOM': 3.20, 'ZUC': 1.49, 'WAT': 3.83,
             'BPEP': 6.85, 'STR': 6.99, 'POT': 0.50, 'SCORN': 0.48, 'CAR': 0.99, 'BEET': 2.50, 'ONS': 0.66, 'RAD': 2.99,
             'SPEA': 3.99, 'LET': 1.99, 'GAR': 3.99, 'BSPR': 7.04, 'KALE': 0.99, 'SPCH': 4.48}

    # A dictionary of the yield per plant (lbs) of each of the crops
    ypp = {'CUC': 2.5, 'EGG': 2.0, 'STOM': 7.0, 'GBEAN': 0.25, 'BSQ': 1.25, 'CTOM': 5.0, 'ZUC': 1.5, 'WAT': 1.0,
           'BPEP': 1.5, 'STR': 0.5, 'POT': 3.0, 'SCORN': 0.25, 'CAR': 1.0, 'BEET': 1.0, 'ONS': 0.3, 'RAD': 0.09,
           'SPEA': 0.25, 'LET': 0.5, 'GAR': 1.0, 'BSPR': 3.0, 'KALE': 0.75, 'SPCH': 0.5}

    # A dictionary of the nutrition density score of each of the crops
    nutrition = {'CUC': 0.0, 'EGG': 0.0, 'STOM': 20.37, 'GBEAN': 0.0, 'BSQ': 13.89, 'CTOM': 0.0, 'ZUC': 0.0, 'WAT': 0.0,
                 'BPEP': 0.0, 'STR': 17.59, 'POT': 0.0, 'SCORN': 0.0, 'CAR': 22.6, 'BEET': 0.0, 'ONS': 0.0,
                 'RAD': 16.91,
                 'SPEA': 0, 'LET': 70.73, 'GAR': 0.0, 'BSPR': 32.23, 'KALE': 49.07, 'SPCH': 86.43}

    # A dictionary of the watering reqs of each of the crops
    water = {'CUC': 4, 'EGG': 4, 'STOM': 4, 'GBEAN': 3, 'BSQ': 4, 'CTOM': 4, 'ZUC': 5, 'WAT': 2, 'BPEP': 3, 'STR': 4,
             'POT': 5, 'SCORN': 4, 'CAR': 5, 'BEET': 4, 'ONS': 4, 'RAD': 2, 'SPEA': 4, 'LET': 4, 'GAR': 4, 'BSPR': 5,
             'KALE': 4, 'SPCH': 4}

    # A dictionary of the value per SQFT of each of the crops
    # MAY NOT BE CORRECT
    valsqft = {'CUC': 3.73, 'EGG': 2.98, 'STOM': 2.96, 'GBEAN': 8.00, 'BSQ': 0.99, 'CTOM': 16.00, 'ZUC': 2.24,
               'WAT': 1.92,
               'BPEP': 10.28, 'STR': 13.98, 'POT': 1.50, 'SCORN': 0.12, 'CAR': 16.50, 'BEET': 22.73, 'ONS': 1.80,
               'RAD': 4.49, 'SPEA': 1.00, 'LET': 3.98, 'GAR': 36.27, 'BSPR': 9.39, 'KALE': 0.74, 'SPCH': 20.36}

    # A dictionary of the total profit of each of the crops
    # MAY NOT BE CORRECT
    total_profit = {'CUC': 2.3, 'EGG': 1.8, 'STOM': 1.8, 'GBEAN': 4.8, 'BSQ': 0.6, 'CTOM': 9.7, 'ZUC': 1.4, 'WAT': 1.2,
                    'BPEP': 6.2, 'STR': 8.5, 'POT': 0.9, 'SCORN': 0.1, 'CAR': 10.0, 'BEET': 13.7, 'ONS': 1.1,
                    'RAD': 2.7,
                    'SPEA': 0.6, 'LET': 2.4, 'GAR': 21.9, 'BSPR': 5.7, 'KALE': 0.4, 'SPCH': 12.3}

    # A dictionary of personal preferences for which plants to grow -> will be user input, could be balanced or nutritional or profit
    # Can we do an if statement here? But how? Need a variable for if user selects bal/nut/or profit/ or own
    manual_preferences = {'CUC': 5, 'EGG': 5, 'STOM': 5, 'GBEAN': 5, 'BSQ': 5, 'CTOM': 5, 'ZUC': 5, 'WAT': 5, 'BPEP': 5,
                          'STR': 5, 'POT': 5, 'SCORN': 5, 'CAR': 5, 'BEET': 5, 'ONS': 5, 'RAD': 5, 'SPEA': 5, 'LET': 5,
                          'GAR': 5, 'BSPR': 5, 'KALE': 5, 'SPCH': 5}

    # A variable to represent the minimum number of plants to crop
    minim = 1

    # A variable to represent the maximum number of plants to crop
    maxim = 8

    # Total amount of a given crop planted should be at least this percent
    plant_at_least = 5

    # Total amount of a given crop planted should be at most this percent
    plant_at_most = 25

    # Total land?
    total_land = 0

    # max land
    max_land = 250

    # Create the 'prob' variable to contain the problem data
    prob = LpProblem("crops to Plant", LpMaximize)

    # A dictionary called 'ingredient_vars' is created to contain the referenced Variables
    crop_vars = LpVariable.dicts("crops", crops, 0)

    # The objective function is added to 'prob' first
    # prob += lpSum([valsqft[i]*crop_vars[i] for i in crops]), "Total Yield Profit is"
    prob += lpSum([manual_preferences[i] * crop_vars[i] for i in crops]), "The optimal solution is"

    # The constraints are added to 'prob'
    prob += lpSum([crop_vars[i] for i in crops]) == 100, "PercentagesSum"
    # time
    prob += lpSum([maintenance[i] * crop_vars[i] for i in crops]) <= time, "TimeRequirement"
    # landSun1
    prob += lpSum([landSun1[i] * crop_vars[i] for i in crops]) <= land1, "LandRequirementSunlight1"
    # landSun2
    prob += lpSum([landSun2[i] * crop_vars[i] for i in crops]) <= land2, "LandRequirementSunlight2"
    # landSun3
    prob += lpSum([landSun3[i] * crop_vars[i] for i in crops]) <= land3, "LandRequirementSunlight3"

    land_per = []
    total_yield = []
    varVal_name = []
    varVal_val = []
    total_val = 0

    # # min number of crops
    # prob += lpSum() >= minim, "MinCropRequirement"  # FIGURE OUT
    # # max number of crops
    # prob += lpSum() <= maxim, "MaxCropRequirement"  # FIGURE OUT
    # # min percent of crop
    # prob += lpSum() >= plant_at_least, "SingleCropMinRequirement"  # FIGURE OUT
    # # max percent of crop
    # prob += lpSum() <= plant_at_most, "SingleCropMaxRequirement"  # FIGURE OUT

    # The problem data is written to an .lp file
    prob.writeLP("DigItProb1.lp")

    # The problem is solved using PuLP's choice of Solver
    print 'PROB:\n'
    prob.solve()

    # The status of the solution is printed to the screen
    print "Status:", LpStatus[prob.status]

    # Each of the variables is printed with it's resolved optimum value
    for v in prob.variables():
        # print v.name, "=", v.varValue
        true_name = str.split(v.name, "_")

        if v.varValue > 0:
            varVal_name.append(true_name[1])
            varVal_val.append(v.varValue)

        list.append(land_per, ((v.varValue * 0.01) * 250))

        total_land += (v.varValue * 0.01) * 250

        total_yield.append(((v.varValue * 0.01) * 250) / land.get(true_name[1]))

        total_val += ((v.varValue * 0.01) * 250) * valsqft.get(true_name[1])

    # The optimised objective function value is printed to the screen
    # print "Value of Produce ($) = ", value(prob.objective)
    # print "Total SQFT = ", total_land
    # print "SQFT per crop: ", land_per
    # print "Yield (# plants) per crop: ", total_yield
    # print "Total Value of Produce ($) = ", total_val
    # print "Total yield = ", total_yield

    result = {}
    result['prob'] = prob
    result['varVal_name'] = varVal_name
    result['varVal_val'] = varVal_val
    result['total_land'] = total_land
    result['land_per'] = land_per
    result['total_yield'] = total_yield
    result['total_val'] = total_val
    return result

