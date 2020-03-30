# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 11:45:47 2019

@author: kjaglicic
"""

# Airflow, setting up DAG

import airflow
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import timedelta


# Setting up default arguments for DAG initialization
default_args = {
        'owner': 'airflow',
        'start_date' : airflow.utils.dates.days_ago(2)
        }


# Initializing our DAG
dag = DAG(
        dag_id = 'DAG_tmp',
        default_args = default_args,
        description = 'DAG for DSC, temporary',
        schedule_interval = timedelta(days=1)
        )


# Defining Tasks
##############

# Reading data


read_data_1 = DummyOperator(
        task_id = 'Read_data_1',
        dag=dag
        )

read_data_2 = DummyOperator(
        task_id = 'Read_data_2',
        dag=dag
        )

read_data_3 = DummyOperator(
        task_id = 'Read_data_3',
        dag=dag
        )

read_data_4 = DummyOperator(
        task_id = 'Read_data_4',
        dag=dag
        )

read_data_5 = DummyOperator(
        task_id = 'Read_data_5',
        dag=dag
        )

read_data_6 = DummyOperator(
        task_id = 'Read_data_6',
        dag=dag
        )

read_data_7 = DummyOperator(
        task_id = 'Read_data_7',
        dag=dag
        )



# Models

task_seq_events = DummyOperator(
        task_id='Sequence_of_impacting_events',
        dag=dag
        )

task_content_ctg = DummyOperator(
        task_id='Content_Categorization',
        dag=dag
        )

task_competitor_call_rec = DummyOperator(
        task_id='Competitor_calls_recognition',
        dag=dag
        )

task_cei = DummyOperator(
        task_id='CEI_Experience_Index',
        dag=dag
        )

task_sna = DummyOperator(
        task_id='Social_Network_Analytics_SNA',
        dag=dag
        )

task_beh_clust = DummyOperator(
        task_id='Behavior_clusters',
        dag=dag
        )

task_offer_optimization = DummyOperator(
        task_id='Offer_optimization',
        dag=dag
        )

task_churn_model = DummyOperator(
        task_id='Churn_prediction_scoring',
        dag=dag
        )

# Making scoring table

making_scoring_table = DummyOperator(
        task_id='Making_scoring_table',
        dag=dag
        )


# Setting up dependecies in our workflow

[read_data_1, read_data_2>>task_seq_events, read_data_3>>task_content_ctg,\
 read_data_4>>task_competitor_call_rec,read_data_5>>task_cei, read_data_6>>task_sna,\
 read_data_7>>task_beh_clust] >> making_scoring_table >> task_churn_model >> task_offer_optimization











