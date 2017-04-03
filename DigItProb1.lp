\* crops to Plant *\
Maximize
The_optimal_solution_is: 5 crops_BEET + 5 crops_BPEP + 5 crops_BSPR
 + 5 crops_BSQ + 5 crops_CAR + 5 crops_CTOM + 5 crops_CUC + 5 crops_EGG
 + 5 crops_GAR + 5 crops_GBEAN + 5 crops_KALE + 5 crops_LET + 5 crops_ONS
 + 5 crops_POT + 5 crops_RAD + 5 crops_SCORN + 5 crops_SPCH + 5 crops_SPEA
 + 5 crops_STOM + 5 crops_STR + 5 crops_WAT + 5 crops_ZUC
Subject To
LandRequirementSunlight1: - crops_BEET - crops_BPEP + 2.3 crops_BSPR
 - crops_BSQ - crops_CAR - crops_CTOM - crops_CUC - crops_EGG + 0.1 crops_GAR
 - crops_GBEAN + crops_KALE + 0.3 crops_LET - crops_ONS - crops_POT
 - crops_RAD - crops_SCORN + 0.1 crops_SPCH - crops_SPEA - crops_STOM
 - crops_STR - crops_WAT - crops_ZUC <= 40
LandRequirementSunlight2: 0.1 crops_BEET + crops_BPEP - 3 crops_BSPR
 - 3 crops_BSQ + 0.1 crops_CAR - 3 crops_CTOM - 3 crops_CUC - 3 crops_EGG
 - 3 crops_GAR - 3 crops_GBEAN - 3 crops_KALE - 3 crops_LET + 0.1 crops_ONS
 + crops_POT + 0.1 crops_RAD + crops_SCORN - 3 crops_SPCH + crops_SPEA
 - 3 crops_STOM + 0.3 crops_STR - 3 crops_WAT - 3 crops_ZUC <= 40
LandRequirementSunlight3: - 3 crops_BEET - 3 crops_BPEP - 3 crops_BSPR
 + crops_BSQ - 3 crops_CAR + crops_CTOM + crops_CUC + crops_EGG - 3 crops_GAR
 + 0.1 crops_GBEAN - 3 crops_KALE - 3 crops_LET - 3 crops_ONS - 3 crops_POT
 - 3 crops_RAD - 3 crops_SCORN - 3 crops_SPCH - 3 crops_SPEA + 4 crops_STOM
 - 3 crops_STR + 2 crops_WAT + crops_ZUC <= 40
PercentagesSum: crops_BEET + crops_BPEP + crops_BSPR + crops_BSQ + crops_CAR
 + crops_CTOM + crops_CUC + crops_EGG + crops_GAR + crops_GBEAN + crops_KALE
 + crops_LET + crops_ONS + crops_POT + crops_RAD + crops_SCORN + crops_SPCH
 + crops_SPEA + crops_STOM + crops_STR + crops_WAT + crops_ZUC = 100
TimeRequirement: 0.001574074 crops_BEET + 0.003148148 crops_BPEP
 + 0.004722222 crops_BSPR + 0.003148148 crops_BSQ + 0.003148148 crops_CAR
 + 0.001574074 crops_CTOM + 0.001574074 crops_CUC + 0.004722222 crops_EGG
 + 0.001574074 crops_GAR + 0.001574074 crops_GBEAN + 0.003148148 crops_KALE
 + 0.001574074 crops_LET + 0.001574074 crops_ONS + 0.001574074 crops_POT
 + 0.001574074 crops_RAD + 0.003148148 crops_SCORN + 0.001574074 crops_SPCH
 + 0.001574074 crops_SPEA + 0.003148148 crops_STOM + 0.003148148 crops_STR
 + 0.004722222 crops_WAT + 0.003148148 crops_ZUC <= 5
End
