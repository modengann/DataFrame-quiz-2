import pandas as pd

def get_role(df):     
    pass

def get_fifth_entry(df):       
    pass

def get_phil_info(df):    
    pass

def get_age_country(df): 
    pass

def get_age_salary_of_middle_three(df):
    pass

def get_role_megan_oscar(df):
    pass

def main():
    df = pd.read_csv("data.csv", index_col= 0)

    print("Role Column:\n", get_role(df))
    print("\nFifth Entry:\n", get_fifth_entry(df))
    print("\nPhil's Info:\n", get_phil_info(df))
    print("\nAge and Country Columns:\n", get_age_country(df))
    print("\nAge and Salary of Middle Three:\n", get_age_salary_of_middle_three(df))
    print("\nRole of Megan and Oscar:\n", get_role_megan_oscar(df))

if __name__ == "__main__":
    main()
