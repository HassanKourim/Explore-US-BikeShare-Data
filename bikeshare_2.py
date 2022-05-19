import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january' , 'february', 'march' ,'april','may','june' ,'all']
days = ['saturday' , 'sunday', 'monday' ,'tuesday' ,'wednesday', "thursday" , "friday" , 'all']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    while True :

        Answer = input("Do you need filter ? yes / no ").lower()

        if Answer == 'yes':    
            print('Hello! Let\'s explore some US bikeshare data!')
            # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
            cities = ['chicago' , 'new york city', 'washington']
            city = input("enter the city from : chicago , new york city , washington :").lower()
            while city not in cities:
                print("Not correct city please enter corect city")
                city = input("enter the city from : chicago , new york city , washington :").lower()

            # get user input for month (all, january, february, ... , june)
            
            month = input("enter the Month from : january , february , march , april ,may,june, all :").lower()
            while month not in months:
                print("Not correct city please enter corect month")
                month = input("enter the Month from : january , february , march , april ,may,june, all :").lower()

            # get user input for day of week (all, monday, tuesday, ... sunday)
            
            day = input("enter the day from : Saturday , sunday , monday , tuesday ,wednesday , thursday , friday , all :").lower()
            while day not in days:
                print("Not correct day please enter corect day")
                day = input("enter the day from : Saturday , sunday , monday , tuesday ,wednesday , thursday , friday , all :").lower()
            break
        elif Answer == 'no' :
            break
        else:
            print("please write a correct word")
            Answer = input("Do you need filter ? yes / no ")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    #convert Start Time column to data time 
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day']= df['Start Time'].dt.day_name

    #filering month 
    if month != "all":
        month = months.index(month) + 1
        df = df[df['month'] == month]

    #filtering day 
    if day != "all":
        day = days.index(day) + 1
        df = df[df['day'] == day.title()]



    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')

    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df["Start Time"])


    # display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print("Popular Month : " , popular_month)

    # display the most common day of week
    df['day']= df['Start Time'].dt.day_name
    popular_day = df['day'].mode()[0]
    print("Popular day : "  ,popular_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("Popular Hour : " , popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df["Start Station"].mode()[0]
    print(popular_start_station)

    # display most commonly used end station
    popular_end_station = df["Start Station"].mode()[0]
    print( "Popular End Station", popular_end_station)

    # display most frequent combination of start station and end station trip
    df['trip']  = df['Start Station'] + df['End Station']
    popular_trip = df["trip"].mode()[0]
    print("Popular Trip" , popular_trip)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df['Start Time'] =pd.to_datetime(df['Start Time'])
    
    # display total travel time
    total_travel = df['Trip Duration'].sum()
    print("Total Travel" , total_travel)
    # display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('mean_travel',mean_travel)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    counts_of_user = df['User Type'].value_counts()
    print('counts_of_user' ,counts_of_user)

    


    # Display earliest, most recent, and most common year of birth
    
    #to avoid error
    try:
        # Display counts of gender
        counts_of_gender = df['Gender'].value_counts()
        print( 'counts_of_gender',counts_of_gender)

        earliest_year = df['Birth Year'].min()
        print("earliest_year",earliest_year)

        most_recent_year = df['Birth Year'].max()
        print("most_recent_year" ,most_recent_year)

        common_year = df['Birth Year'].mode()[0]
        print("Common Year", common_year)


    except:
        print(" no column is call that ")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        # Ask the User if you would like to display the raw 
        res = input("Would you like to display raw data ? ").lower()
        while res == "yes":
            print(df.sample(5))
            res = input("Would you like to display raw data ? ").lower()
          
        # Ask the User if you would like to restart 
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
