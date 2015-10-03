from Levenshtein import ratio


def getMatchItem(ayah):
	matchItem = {
		"surahNum": 0,
		"ayahNum": 0,
		"englishSurahName": "",
		"arabicSurahName": "",
		"arabicAyah": "",

	}
	
	arabicAyah = ayah["aya"]["text"].encode("utf-8")

	while arabicAyah.find("<span") > -1:
		startSpan1 = arabicAyah.find("<span")
		endSpan1 = arabicAyah.find(">") + 1
		arabicAyah = arabicAyah[:startSpan1] + arabicAyah[endSpan1:]

		startSpan2 = arabicAyah.find("</span>")
		endSpan2 = arabicAyah.find("</span>") + 7
		arabicAyah = arabicAyah[:startSpan2] + arabicAyah[endSpan2:]

	matchItem["surahNum"] = ayah["sura"]["id"]
	matchItem["ayahNum"] = ayah["aya"]["id"]
	matchItem["englishSurahName"] = ayah["sura"]["english_name"]
	matchItem["arabicSurahName"] = ayah["sura"]["arabic_name"]
	matchItem["arabicAyah"] = arabicAyah

	return matchItem

def mostCommon(spoken, lst):
	highestCountItem = max(lst, key=lst.count)
	highestCount = lst.count(highestCountItem)
	contenders = []
	for item in lst:
		if (lst.count(item) == highestCount) and (item not in contenders):
			contenders.append(item)
	if len(contenders) > 1:
		# print contenders
		print "\nContending"
		bestMatch = ["None", 0]
		for ayah in contenders:
			score = ratio(spoken, ayah["arabicAyah"])
			print ayah["arabicAyah"]
			print score
			if score > bestMatch[1]:
				bestMatch = [ayah, score]
		return bestMatch[0]
	else:
		return highestCountItem

def printResults(ayah):
		print " "
		print (str(ayah["surahNum"]) + ":" + str(ayah["ayahNum"]) + ", " + ayah["englishSurahName"] + " | " + ayah["arabicSurahName"]).encode("utf-8")
		print "Ayah: " + ayah["arabicAyah"]
		print " "

