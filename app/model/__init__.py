from app.db import Connection
class State:
    def __init__(self):
        self.db = Connection()

    def create(self, name, abbreviation, capital,population, year_admitted):
        """
        this function creates a new state
        """

        self.name = name
        self.abbreviation = abbreviation
        self.capital=capital
        self.population=population
        self.year_admitted=year_admitted

        # State data      
        state=(self.name,self.abbreviation,self.capital,self.population,self.year_admitted)

        query = "INSERT INTO states (name, abbreviation, capital,population, year_admitted) VALUES(%s,%s,%s,%s,%s)"

        # Execute query that inserts state data into the database
        self.db.cursor.execute(query, state)

        result=self.db.cursor.rowcount

        if result:
            self.db.conn.commit()
            return True

        # Commit data to the database
        
        # Close cursor
        self.db.cursor.close()
        # Close connection
        self.db.conn.close()

    def get_States(self):
        """
        this function lists all states
        """
        query="SELECT * FROM states"

        self.db.cursor.execute(query)

        # Retrieve the user record in the database: returns a tuple
        results=self.db.cursor.fetchall()

        # Close cursor
        self.db.cursor.close()
        # Close connection
        self.db.conn.close()

        return results
    
    def update_State(self,id,population):
        """
        this function updates a states' population
        """
        self.id=id
        self.population=population
        
        data=(self.population, self.id)
        query="UPDATE states SET population=%s WHERE id=%s"
        
        self.db.cursor.execute(query,data)

        result=self.db.cursor.rowcount
        print (result)

        if result:  
            self.db.conn.commit()
            return True

        # Close cursor
        self.db.cursor.close()
        # Close connection
        self.db.conn.close()

    def delete_State(self,id):
        """
        this function deletes a state
        """
        self.id=id

        query="DELETE FROM states WHERE id=%s"

        self.db.cursor.execute(query,[self.id])

        result=self.db.cursor.rowcount

        print (result)
        if result:  
            self.db.conn.commit()
            return True
        
        # Close cursor
        self.db.cursor.close()
        # Close connection
        self.db.conn.close()
        
    def filter_State_Starting_with_A(self):
        """
        this function filters all states staring with letter 'A'
        """
        query="SELECT * FROM states WHERE name LIKE 'A%'"

        self.db.cursor.execute(query)

        result=self.db.cursor.fetchall()
        for row in result:
            print(row)
    
        #Close cursor
        self.db.cursor.close()
        # Close connection
        self.db.conn.close()

        return result
    
    def search_State_By_Name(self,name):
        """
        this functions searches for state details by name
        """
        query="SELECT * FROM states WHERE name=%s"

        self.db.cursor.execute(query,[name])

        result=self.db.cursor.fetchall()
        for row in result:
            print(row)

        #Close cursor
        self.db.cursor.close()
        # Close connection
        self.db.conn.close()

        return result
    
    def list_State_Capital(self):
        """
        this function lists state capitals in ascending format
        """
        query="SELECT capital from states"

        self.db.cursor.execute(query)

        result=self.db.cursor.fetchall()
        for row in result:
            print (row)

        #Close cursor
        self.db.cursor.close()
        # Close connection
        self.db.conn.close()

        return result
    
    def find_Most_Populous_State(self):
        """
        this function finds most populous states
        """
        query="SELECT MAX(population) FROM states"

        self.db.cursor.execute(query)

        result=self.db.cursor.fetchall()
        for row in result:
            print (row)

        #Close cursor
        self.db.cursor.close()
        # Close connection
        self.db.conn.close()

        return result
    
    def average_Population(self):
        """
        this function finds average of populations
        """
        query="SELECT AVG(population) FROM states"

        self.db.cursor.execute(query)

        result=self.db.cursor.fetchall()
        for row in result:
            print (row)

        #Close cursor
        self.db.cursor.close()
        # Close connection
        self.db.conn.close()

        return result
    
    def states_Admitted_Between_1750_And_1850(self):
        """
        this function lists states admitted between 1750 and 1850
        """
        query="SELECT * FROM states WHERE year_admitted BETWEEN 1750 AND 1850"

        self.db.cursor.execute(query)

        result=self.db.cursor.fetchall()
        for row in result:
            print (row)

        #Close cursor
        self.db.cursor.close()
        # Close connection
        self.db.conn.close()

        return result
    
    def count_States_By_Population(self):
        """
        this function counts states by population range
        """
        query="SELECT COUNT(id) FROM states WHERE population BETWEEN 1000000 AND 5000000"

        self.db.cursor.execute(query)

        result=self.db.cursor.fetchall()
        for row in result:
            print (row)

        #Close cursor
        self.db.cursor.close()
        # Close connection
        self.db.conn.close()

        return result
