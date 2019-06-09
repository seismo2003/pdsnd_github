## Python final Project
import time
import pandas as pd
import numpy as np
import datetime

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
    city = input("Please choose your favorite city to analyze:").lower()
    city_list = ['chicago','new york city','washington']
    while city not in city_list:
        print("The city you entered is not in our library, please re-enter city name again")
        city = input("Please choose your favorite city to analyze:").lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Please choose the month/months you want to analyze:").lower()
    month_list = ['january','february','march','april','may','june','all']
    while month not in month_list:
        print("The month you entered is not in our library, please re-enter month name again")
        month = input("Please choose the month/months you want to analyze:").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please choose the day of week you want to analyze:").lower()
    day_list = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
    while day not in day_list:
        print("The city you entered is not in our library, please re-enter city name again")
        day = input("Please choose the day of week you want to analyze:").lower()

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
    df['month'] = pd.to_datetime(df['Start Time']).dt.month
    df['day'] = pd.to_datetime(df['Start Time']).dt.weekday_name

    if month != 'all':
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day'] == day.title()]

#    print(df)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month is: ", common_month)

    # TO DO: display the most common day of week
    common_day = df['day'].mode()[0]
    print("The most common day is: ", common_day)
    # TO DO: display the most common start hour
    df['hour'] = pd.to_datetime(df['Start Time']).dt.hour
    common_start_hour = df['hour'].mode()[0]
    print("The most common start hour is: ", common_start_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_st = df["Start Station"].mode()[0]
    print("The most common start station is:", common_start_st)
    # TO DO: display most commonly used end station
    common_end_st = df["End Station"].mode()[0]
    print("The most common end station is:", common_end_st)
    # TO DO: display most frequent combination of start station and end station trip
    df["common_route"] = df['Start Station'] + ' to ' + df['End Station']
    common_route = df["common_route"].mode()[0]
    print("The most common route is:", common_route)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is:", total_travel_time)
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time is:", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Display user types:  ", user_types)

    # TO DO: Display counts of gender
    gender = df['Gender'].value_counts()
    print("Display gender: ", gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    #df['Earliest Birth Year'] = df['Birth Year'].fillna(0)
    #earliest_yob = df['Birth Year'].sort_values(ascending = True).head(1).item()
    earliest_yob = df['Birth Year'].describe()['min']
    print("The earliest year of birth is:", earliest_yob)
    #current_yr = datetime.datetime.now().year
    recent_yob = df['Birth Year'].describe()['max']
    #df['Most Recent Birth Year'] = df['Birth Year'].fillna(current_yr)
    #recent_yob = df['Birth Year'].sort_values(ascending = False).head(1).item()
    print("The most recent year of birth is:", recent_yob)
    common_yob = df['Birth Year'].mode()[0]
    print("The most common year of birth is:", common_yob)

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
        df = df.drop('common_route', axis = 1)
        df = df.drop('hour', axis = 1)
        df = df.drop('day', axis = 1)
        df = df.drop('month', axis = 1)
        raw_data = input('\nWould you like to see raw data? Enter yes or no.\n')
        count = 0
        while raw_data.lower() == 'yes':
            print(df.iloc[count:count + 5])
            raw_data = input('\nWould you like to see raw data? Enter yes or no.\n')
            count += 5
            if count > len(df) - 5:
                count = 0
            else:
                continue
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
