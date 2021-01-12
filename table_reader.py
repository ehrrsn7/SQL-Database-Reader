"""
Table Reader module
Import this using python to get access to helper methods for reading database.db files
"""

class table_reader:
    """import this module to access tables within database"""
    def __init__(self, database_filename: str, table_name: str):
        self.database   = database_filename
        self.table      = table_name
        
        # set self.connection and self.cursor

    # define method for resetting self.connection and self.cursor

    # define helper methods for reading, appending, deleting and updating files

    # define user interaction methods which call above helper methods