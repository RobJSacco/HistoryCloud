
# HistoryCloud
A tool developed to parse major news websites, to convert the headlines of the day into a word cloud that changes over time

## CLI
HistoryCloud.py will require inputs of cloud startdate and enddate initially
Later, the project can be expanded to allow optional inputs of frame requirement, weekly, monthly or yearly spacing, final gif (soft ‘G,’ pronounced ‘jif’) name, and cloud averaging

## frequency_data Obj
 frequency_data() object holds the keyword, and the number of times the keyword comes up in an object
* frequency_data.add(Keyword,Count)
* str[] keyword = frequency_data.Keyword()
* int[] count = frequency_data.Count()


## WebScraper

```
cloudscraper(Date){
  
  frequency_Data = FrequncyData()
  //Code that scrapes a webpage and writes keywords to frequency_data    
  returns frequency_data
}
```

## cloud_builder

```
cloud_builder(frequency_data){
  //Code that Makes a WordCloud PNG
  f.save(FolderName/Cloud.png)  
  Return FolderName
}
```

### cloud_stitcher

```
cloud_stitcher(FolderName, GifName){
  //Code that stiches the images into a GIF
  f.save(GifName.gif)
}

```
