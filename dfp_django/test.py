for l in lines:
    for s in ["anat","rest_CAP"]:
        print "adding %s:%s to %s"%(l,s,p1.doi)
        try:
            d=Data.objects.get(individual=l,scan_type=s)
            d.paper.add(p1)
        except Data.DoesNotExist:
            print "%s:%s could not be found in data"%(l,s)