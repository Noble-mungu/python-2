import os
class  Config:
	'''
	General configuration parnet class
	'''

class Production(Config):

	'''
	Production configuration child class
    

	Args:
	Config:The parent configuration class with general configuration settings
	 '''
	pass

class DevConfig(Config):
     '''
     Development configuration child class

     Args:
     Config:The parent configuration class with General settings

     '''     
     DEBUG = True
config_option = {
	#Enables us to access different configuration option classes.
    'development':DevConfig,
    'production':ProdConfig

} 



