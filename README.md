# HistoryCloud
A tool developed to parse major news websites, to convert the headlines of the day into a word cloud that changes over time

## CLI
HistoryCloud.py will require inputs of cloud startdate and enddate initially
Later, the project can be expanded to allow optional inputs of frame requirement, weekly, monthly or yearly spacing, final gif name, and cloud averaging

## FrequencyData Obj
 FrequencyData() object holds the keyword, and the number of times the keyword comes up in an object
* FrequencyData.add(Keyword,Count)
* str[] keyword = FrequencyData.Keyword()
* int[] count = FrequencyData.Count()


## WebScraper

```
CloudScraper(Date){
  
  FrequencyData = FrequncyData()
  //Code that scrapes a webpage and writes keywords to FrequencyData    
  returns FrequencyData
}
```

## CloudBuilder

```
CloudBuilder(FrequencyData){
  //Code that Makes a WordCloud PNG
  f.save(FolderName/Cloud.png)  
  Return FolderName
}
```

### CloudSticher

```
CloudSticher(FolderName, GifName){
  //Code that stiches the images into a GIF
  f.save(GifName.gif)
}

```
