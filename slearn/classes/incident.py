"""
Created on July 10, 2018

@author: marcel.zoll
"""

class Incident(object):
    """ define a Incident as a stateful blob of new information
    
    Parameters
    ----------
    uid : obj
        an unique ID as a global unique identifier of this object and its contents
    targetid : obj 
        an unique ID (typically UserKey) which can be locally clustered, and signals a grouping
    timestamp : datetime.datetime
        timestamp for sequence order

    Attributes
    ----------
    meta : dict
        meta-information on this object
    data : dict
        holds the new input information 
    """
    def __init__(self, uid, targetid, timestamp, meta={}, data={}):
        self.uid = uid
        self.targetid = targetid
        self.timestamp = timestamp
        self.meta = meta
        self.data = data

    def __str__(self):
        return f"Incident(uid:{self.uid}, tid:{self.targetid}, ts:{self.timestamp})::" + \
               "data:{{{}}}".format(list(self.data.keys()))
