# Alias
from IPL2021 import venue
from IPL2021.RCB.KKR import KKRvenue as KKRModule
from IPL2021.RCB import RCBvenue as RCBModule

venue.printVenue()

KKRModule.printVenue()
RCBModule.printVenue()

# Approach 2
from IPL2021.venue import printStadium as defStadium
from IPL2021.RCB.KKR.KKRvenue import printStadium as KKRStadium
from IPL2021.RCB.RCBvenue import printStadium as RCBStadium

# printStadium()
defStadium()
KKRStadium()
RCBStadium()