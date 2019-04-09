import cacheTable

cdef class cacheWrap:
  cdef public object cache

  def __cinit__(self,object cacheTemp):
    assert isinstance(cacheTemp, object)
    self.cache = cacheTemp

  def __init__(self, cacheTemp):
    self.cache = cacheTemp
