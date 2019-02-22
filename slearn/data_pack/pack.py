"""
Created on Feb 17, 2019

@author: marcel.zoll
"""


class DataPack(object):
    """ collection holding data representing any of the internal classes
    
    Attributes
    ----------
    cls : class
        class this object is keyed to
    data : pandsa.DataFrame
        a pandas data frame holding the relkevant data
    header_fnames : list of str
        holds the field names for the header
    data_fanmes : list of str
        holds the field names for the data
    meta_fanmes : list of str
        _holds the names of the meta info
    """

    def __init__(self, cls, data_df, uid_fname, targetid_fname, timestamp_fname, meta_fnames, data_fnames):
        self.cls = cls
        self.data_df = data_df,
        self.uid_fname = uid_fname
        self.targetid_fname = targetid_fname
        self.timestamp_fname = timestamp_fname
        self.data_fnames = data_fnames
        self.meta_fnames = meta_fnames

    def startTime(self):
        return self.data_df[self.timestamp_fname].min()

    def endTime(self):
        return self.data_df[self.timestamp_fname].max()

    def copy(self):
        return DataPack(
            self.cls,
            self.data_df.copy(),
            self.uid_fname, self.targetid_fname, self.timestamp_fname,
            self.meta_fnames.copy(),
            self.data_fnames.copy())

    def __len__(self):
        return len(self.data_df)

    @property
    def uid(self):
        return self.data_df[self.uid_fname]
    @property
    def targetid(self):
        return self.data_df[self.targetid_fname]
    @property
    def timestamp(self):
        return self.data_df[self.timestamp_fname]
    @property
    def meta(self):
        return self.data[self.meta_fnames]

    @property
    def data(self):
        return self.data[self.data_fnames]

    def append(self, other):
        """ append another object of the same class as this, where the data is the union of both """
        assert(isinstance(other, self.__class__))
        assert(other.cls == self.cls)

    def items(self):
        """ get the item representation of the data in this object """
        objs = []
        for i in range(len(self)):
            obj = self.cls(
                uid=self.uid_fanme, targetid=self.targetid_fname, timestamp=self.timesstamp_fname,
                data=self.data.iloc[i].as_dict(),
                meta=self.meta.iloc[i].as_dict())
            objs.append(obj)
        return objs
