class config:
	'''
	General configuration parnet class
	'''

class Production(config):

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
     Config:The parent configuration clas with General settings

     '''     
     DEBUG = True
config_option = {
	#Enables us to access different configuration option classes.
    'development':DevConfig,
    'production':ProdConfig

} 



