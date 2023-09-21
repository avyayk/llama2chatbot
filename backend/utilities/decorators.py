
# ~ Singleton class decorator ~
def SingletonClass( class_ ):
    
    # Holds class "instances"
    instances = {}

    # Method to get single instance
    def get_instance( *args, **kwargs ):
        
        # If object does not have an instance, create one
        if class_ not in instances:
            instances[ class_ ] = class_( *args, **kwargs )
        
        return instances[ class_ ]

    return get_instance
