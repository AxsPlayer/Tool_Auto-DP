# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
This File is designed to convert raw data set into suitable format for Machine Learning Algorithm.
"""
# Import necessary packages.
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


def delete_rows(data, cutoff=0):
    """Delete unnecessary rows in dataframe.

    Delete duplicate rows in dataframe, as well as deleting some rows
    whose rating is under cutoff.

    :param data: The input Pandas Dataframe.
    :param cutoff: Numerical value. Default value is 0, meaning if
                rating score is equals or under cutoff.

    :return: Dataframe with remaining rows.
    """
    # Delete duplicate rows.
    column_names = data.columns.values
    data = data.drop_duplicates(subset=column_names[0:2],
                                keep='first')

    # Delete useless rows with ratings under cutoff.
    data = data[data[column_names[2]] > cutoff]

    return data


def convert_process(data, split=False, split_ratio=0.2, fill_num=0):
    """Convert raw data into suitable format.

    This function is designed to fixed data format into suitable data format
    which would be feed into machine learning algorithms.

    :param data: The input data, in format of Pandas Dataframe.
                The data structure should be as following:
                eg.
                |   user_id   |  item_id   |   score   |
                |      1      |     3      |    6.5    |
    :param split: Boolean value. Default value is False. If True, the data set
                will be split into two part, one for training and one for validation.
    :param split_ratio: Numerical value. Default value is 0.2, which means the ratio of
                        number of validation data to total data is 0.2.
    :param fill_num: Numerical value. Default value is 0, which means filling NA value with 0.

    :return: Suitable dataframe format.
            If split is True, return training_dataframe, validation_dataframe.
            If split is False, return training_dataframe.
    """
    # Drop duplicate rows, as well as some rows with ratings which provides not real scores.
    data = delete_rows(data)

    # Convert data into UxM-Matrix.
    rating_matrix = data.reset_index().pivot(index=data.columns.values[0],
                                             columns=data.columns.values[1],
                                             values=data.columns.values[2])

    # Fill Na with fill_num.
    rating_matrix = rating_matrix.fillna(fill_num)

    # Check split value, if true, split data into train and validation dataframe.
    if split:
        train_matrix, validation_matrix = train_test_split(rating_matrix,
                                                           test_size=split_ratio,
                                                           random_state=36)

        return train_matrix, validation_matrix
    else:
        return rating_matrix
