import shapely
from shapely.ops import unary_union

# THIS FILE CONTAINS ALL OF THE ALTERYX AGGREGATION FUNCTIONS

aggregator_fns = {}

def summary_sum(x,xml=None):
    return sum(x)
aggregator_fns['Sum'] = summary_sum

def summary_min(x,xml=None):
    return x.min()
aggregator_fns['Min'] = summary_min

def summary_max(x,xml=None):
    return x.max()
aggregator_fns['Max'] = summary_max

def summary_concat(x,xml=None):
    start = xml.find('Concat_Start').text
    sep = xml.find('Separator').text
    end = xml.find('Concat_End').text
    return start + x.str.cat(sep=sep) + end
aggregator_fns['Concat'] = summary_concat

def summary_count(x,xml=None):
    return len(x)
aggregator_fns['Count'] = summary_count

def summary_first(x,xml=None):
    print("FIRST----")
    print(x)
    return x.iloc[0]
aggregator_fns['First'] = summary_first

def summary_last(x,xml=None):
    print("LAST----")
    print(x)
    return x.iloc[-1]
aggregator_fns['Last'] = summary_last

def summary_longest(x,xml=None):
    print("LONGEST----")
    string_lengths = x.str.len()
    max_length = string_lengths.max()
    longest_strings = x[string_lengths == max_length]
    print(x.dtype)
    return longest_strings.iloc[0]
aggregator_fns['Longest'] = summary_longest

def summary_shortest(x,xml=None):
    print("SHORTEST----")
    string_lengths = x.str.len()
    min_length = string_lengths.min()
    longest_strings = x[string_lengths == min_length]
    return longest_strings.iloc[0]
aggregator_fns['Shortest'] = summary_shortest

def summary_avg(x,xml=None):
    print('AVERAGE')
    print(x.mean())
    return x.mean()
aggregator_fns['Avg'] = summary_avg

def summary_median(x,xml=None):
    print('MEDIAN')
    print(x.median())
    return x.median()
aggregator_fns['Median'] = summary_median

def summary_mode(x,xml=None):
    print('MODE')
    print(x.mode())
    return x.mode().iloc[0]
aggregator_fns['Mode'] = summary_mode

def summary_std(x,xml=None):
    print("STD")
    print(x.std())
    return x.std()
aggregator_fns['StdDev'] = summary_std

def summary_var(x,xml=None):
    print("VAR")
    print(x.var())
    return x.var()
aggregator_fns['Variance'] = summary_var

def summary_spatialCombine(x,xml=None):
    print("SpatialObjCombine")
    return unary_union(x)
aggregator_fns['SpatialObjCombine'] = summary_spatialCombine

def summary_convexHull(x,xml=None):
    print("SpatialObjConvexHull")
    return unary_union(x).convex_hull
aggregator_fns['SpatialObjConvexHull'] = summary_convexHull

def summary_countBlanks(x,xml=None):
    print("summary_countBlanks")
    filtered_series = x.loc[lambda x: x.isna() | (x == '')]
    print(len(filtered_series))
    return len(filtered_series)
aggregator_fns['CountBlank'] = summary_countBlanks

def summary_countNonBlanks(x,xml=None):
    print("CountNonBlank")
    filtered_series = x.dropna().loc[lambda a: a != '']
    print(len(filtered_series))
    return len(filtered_series)
aggregator_fns['CountNonBlank'] = summary_countNonBlanks
