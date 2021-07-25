import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = str(input('Select a city (Chicago, New York City, Washington): ').lower().strip())
        if city in ['chicago','new york city','washington']:
            break
        else:
            print('Please select a city from the list.')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = str(input('Select a filter for the month: (January, February, March, April, May, June, or All) ').title().strip())
        if month in ['January','February','March','April','May','June','All']:
            break
        else:
            print('Please select a filter from the list.')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = str(input('Select a filter for the day: (Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or All) ').title().strip())
        if day in ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'All']:
            break
        else:
            print('Please select a filter from the list.')

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

    # load the data file for the specified city into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime and extract month and day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # apply a filter for the month
    if month != 'All':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # apply a filter for the day
    if day != 'All':
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Common Month:', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Common Day of Week:', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Common Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Common End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Trip'] = "From "+df['Start Station']+" to "+df['End Station']
    popular_trip = df['Trip'].mode()[0]
    print('Most Common Trip:', popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_duration = df['Trip Duration'].sum()
    print('Total Travel Time:', total_trip_duration)

    # TO DO: display mean travel time
    mean_trip_duration = df['Trip Duration'].mean()
    print('Mean Travel Time:', mean_trip_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def identity_stats(df):
    """Displays statistics on gender and birth year of bikeshare users."""

    print('\nCalculating Identity Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of gender and earliest, most recent, and most common year of birth
    while True:
        try:
            gender = df['Gender'].value_counts()
            print(gender)
            min_birth_year = df['Birth Year'].min()
            max_birth_year = df['Birth Year'].max()
            popular_birth_year = df['Birth Year'].mode()[0]
            print('Earliest Year of Birth:', min_birth_year)
            print('Most Recent Year of Birth:', max_birth_year)
            print('Most Common Year of Birth:', popular_birth_year)
            break
        except KeyError:
            print('Gender and Birth Year Statistics Are Not Available for Washington')
            break


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Asks user to view rows of individual trip data, it displays 5 rows each time."""

    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no.\n')
    start_loc = 0

    # TO DO: Create a loop that breaks when the user enter "no" and display 5 rows each time
    while (view_data != 'no'):
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_data = input("Do you wish to continue? Enter yes or no.\n").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

         # TO DO: Implement a logic that interacts with the user and asks for the statistics he/she wants to display
        step_1 = input('\nWould you like to display statistics on the most frequent times of travel? Enter yes or no.\n')
        if step_1.lower() == 'yes':
            time_stats(df)
        step_2 = input('\nWould you like to display statistics on the most popular stations and trip? Enter yes or no.\n')
        if step_2.lower() == 'yes':
            station_stats(df)
        step_3 = input('\nWould you like to display statistics on trip duration? Enter yes or no.\n')
        if step_3.lower() == 'yes':
            trip_duration_stats(df)
        step_4 = input('\nWould you like to display statistics on bikeshare users? Enter yes or no.\n')
        if step_4.lower() == 'yes':
            user_stats(df)
        step_5 = input('\nWould you like to display statistics on gender and birth year of bikeshare users? Enter yes or no.\n')
        if step_5.lower() == 'yes':
            identity_stats(df)

        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
