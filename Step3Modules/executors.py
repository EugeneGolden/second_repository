__author__ = 'Admin'

import filters
import processors
import providers

filename = "pol.txt"
fp = providers.FileProcessor(filename)
wc = processors.WordsCalculator()
#fp.processFile(wc)
#lwc = LowerCaseFilter( wc )
#filterforwc = OnlyLongLinesFilter( lwc )
#fp.processFile(filterforwc)
#filterforwc = OnlyLongLinesFilter( wc )
#fp.processFile( filterforwc )
#lwc = LowerCaseFilter( wc )
#ollf = OnlyLongLinesFilter( lwc );
#fp.processFile( ollf )
rw = filters.RemoveVowels( wc )
fp.processFile( rw )
print "This is results of words counting regarding file %s:" % filename, wc.getDict()
