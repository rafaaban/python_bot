import os

class Config(object):
	SECRET_KEY = 'jijiji'
	PAGE_ACCESS_TOKEN = 'EAAZA3KNW4TVkBADWSEsT8b7rn63kVOoMXADJ9PJUauOwqmfBjAmewa4w5BHSJMtIONZCIRZCpDt9SBSjg7ZCJoFLt4WdURHrwFeX2ioRfgALjow3bxjF6ZCOPwZBHuKI860VHkRXf5Mmj5LME14BJZACEdlq2zDCSTBRTOFB7ZAXNgZDZD'


class DevelopmentConfig(Config):
	DEBUG = True

class ProductionConfig(Config):
	DEBUG = False

	