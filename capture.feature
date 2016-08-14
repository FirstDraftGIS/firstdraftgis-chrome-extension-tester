Feature: capture place

    Scenario Outline: capture locations from pages
         When go to <url>
          And wait 10 seconds
          And go to about:blank
          And wait 1 second
          And open popup
          And wait 1 second
         Then <name> should appear in popup

    Examples: Wikipedia Locations
        | url | name |
        | https://en.wikipedia.org/wiki/Detroit | Detroit |
        | http://www.openstreetmap.org/relation/1671018 | Izmaylovsky Park |
        | https://www.openstreetmap.org/node/618035478#map=13/19.6007/-72.7815 | Terre Neuve |
        #| https://www.openstreetmap.org/way/365019865#map=13/38.8779/-76.9920 | Anacostia River |
        | https://www.flickr.com/photos/usnationalarchives/7159000676 | Leo Carrillo state park |
