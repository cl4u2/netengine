"""
NetEngine SNMP Ubiquiti Air OS backend
"""

__all__ = ['AirOS']


from datetime import timedelta

from netengine.backends.snmp import SNMP


class AirOS(SNMP):
    """
    Ubiquiti AirOS SNMP backend
    """
    
    def __str__(self):
        """ print a human readable object description """
        return u"<SNMP (Ubiquity AirOS): %s>" % self.host
    
    def validate(self):
        """
        raises NetEngineError exception if anything is wrong with the connection
        for example: wrong host, invalid community
        """
        self.name
    
    @property
    def os(self):
        """
        returns (os_name, os_version)
        """
        os_name = 'AirOS'
        os_version = self.get_value('1.2.840.10036.3.1.2.1.4.8')
        return os_name, os_version
    
    @property
    def name(self):
        """
        returns a string containing the device name
        """
        return self.get_value('1.3.6.1.2.1.1.5.0')
    
    @property
    def model(self):
        """
        returns a string containing the device model
        """
        return self.get_value('1.2.840.10036.3.1.2.1.3.8')
    
    @property
    def ssid(self):
        """
        returns a string containing the wireless ssid
        """
        return self.get_value('1.2.840.10036.1.1.1.9.8')
    
    @property
    def uptime(self):
        """
        returns an integer representing the number of seconds of uptime
        """
        return int(self.get_value('1.3.6.1.2.1.1.3.0')) / 100
    
    @property
    def uptime_tuple(self):
        """
        returns (days, hours, minutes)
        """
        td = timedelta(seconds=self.uptime)
        
        return td.days, td.seconds//3600, (td.seconds//60)%60