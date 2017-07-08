# Add your imports here - SK Learn, Pandas, Keras (only what you need needs imported)
import numpy as np
import pandas as pd
import csv

from sklearn.naive_bayes import MultinomialNB

combined_collision_df = pd.read_csv('combined_collision.csv')

def predict_ni():
    combined_collision_df = pd.read_csv('combined_collision.csv')
    clf = combined_collision_df

    collision_data = combined_collision_df
    np.array(collision_data)
    classes = np.array(collision_data['a_type'])
    clf = MultinomialNB()
    clf.fit(collision_data, classes)
    MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
    print clf.predict_proba(collision_data).mean(0)
    return clf.predict_proba(collision_data).mean(0)

def predict_area(area_code):
    combined_collision_df = pd.read_csv('combined_collision.csv')
    clf = combined_collision_df

    combined_collision_df = combined_collision_df[combined_collision_df['a_District'] == area_code]
    collision_data = combined_collision_df
    np.array(collision_data)
    classes = np.array(collision_data['a_type'])
    clf = MultinomialNB()
    clf.fit(collision_data, classes)
    MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
    print clf.predict_proba(collision_data).mean(0)
    return clf.predict_proba(collision_data).mean(0)

def num_of_casualties():
    collision2015_df = pd.read_csv('collision2015.csv')
    collision2014_df = pd.read_csv('collision2014.csv')
    collision2013_df = pd.read_csv('collision2013.csv')

    combined_total = len(collision2015_df) + len(collision2014_df) + len(collision2013_df)
    print combined_total
    return combined_total

def num_of_fatalities():
    collision2015_df = pd.read_csv('collision2015.csv')
    collision2015_df = collision2015_df[collision2015_df['a_type'] == 1]
    collision2014_df = pd.read_csv('collision2014.csv')
    collision2014_df = collision2014_df[collision2014_df['a_type'] == 1]
    collision2013_df = pd.read_csv('collision2013.csv')
    collision2013_df = collision2014_df[collision2014_df['a_type'] == 1]

    combined_total_of_fatalities = len(collision2015_df) + len(collision2014_df) + len(collision2013_df)
    print combined_total_of_fatalities
    return combined_total_of_fatalities

def num_of_serious():
    collision2015_df = pd.read_csv('collision2015.csv')
    collision2015_df = collision2015_df[collision2015_df['a_type'] == 2]
    collision2014_df = pd.read_csv('collision2014.csv')
    collision2014_df = collision2014_df[collision2014_df['a_type'] == 2]
    collision2013_df = pd.read_csv('collision2013.csv')
    collision2013_df = collision2014_df[collision2014_df['a_type'] == 2]

    combined_total_of_serious = len(collision2015_df) + len(collision2014_df) + len(collision2013_df)
    print combined_total_of_serious
    return combined_total_of_serious

def num_of_slight():
    collision2015_df = pd.read_csv('collision2015.csv')
    collision2015_df = collision2015_df[collision2015_df['a_type'] == 3]
    collision2014_df = pd.read_csv('collision2014.csv')
    collision2014_df = collision2014_df[collision2014_df['a_type'] == 3]
    collision2013_df = pd.read_csv('collision2013.csv')
    collision2013_df = collision2014_df[collision2014_df['a_type'] == 3]

    combined_total_of_slight = len(collision2015_df) + len(collision2014_df) + len(collision2013_df)
    print combined_total_of_slight
    return combined_total_of_slight

def find_average_total():
    combined_df = pd.read_csv('combined.csv')

    average_hour = sum(combined_df['a_hour'])/len(combined_df['a_hour'])
    average_min = sum(combined_df['a_min'])/len(combined_df['a_min'])
    print str(average_hour) + ":" + str(average_min)
    return str(average_hour) + ":" + str(average_min)

def find_average_of_type(data_type):
    combined_df = pd.read_csv('combined.csv')
    combined_df = combined_df[combined_df['a_type'] == data_type]

    average_hour = sum(combined_df['a_hour'])/len(combined_df['a_hour'])
    average_min = sum(combined_df['a_min'])/len(combined_df['a_min'])
    print str(average_hour) + ":" + str(average_min)
    return str(average_hour) + ":" + str(average_min)