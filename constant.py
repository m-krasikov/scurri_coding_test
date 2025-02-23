import re

AA9 = re.compile(r"^[A-PR-UWYZ][A-HK-Y][0-9]$")
AA99 = re.compile(r"^[A-PR-UWYZ][A-HK-Y][0-9]{2}$")
A9_A99 = re.compile(r"^[BEGL-NSW][0-9]{1,2}$")
A9A = re.compile(r"^[ENW][1][A-HJKPS-UW]$")
AA9A = re.compile(r"^([WC[0-9]|EC[1-4]|SW1|][ABEHMNPRV-Y])|(NW1W|SE1P)$")
INWARD_CODE_PATTERN = r"^[0-9][ABD-HJLNP-UW-Z]{2}$"

SINGLE_DIGIT_DISTRICT_AREAS = ("BL", "BR", "FY", "HA", "HD", "HG", "HR", "HS", "HX", "JE", "LD", "SM", "SR", "WN", "ZE")
DOUBLE_DIGIT_DISTRICT_AREAS = ("AB", "LL", "SO")
ZERO_DISTRICT_AREAS = ("BL", "BS", "CM", "CR", "FY", "HA", "PR", "SL", "SS")

OUTWARD_CODE_PATTERNS = {
    "AA9": AA9,
    "AA99": AA99,
    "A9|A99": A9_A99,
    "A9A": A9A,
    "AA9A": AA9A,
}
