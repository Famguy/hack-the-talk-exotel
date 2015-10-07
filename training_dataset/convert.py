from pydub import AudioSegment
import glob

emotions = ['angry','neutral','unhappy','happy']

for e in emotions:
	emolist = glob.glob(e+'/*.mp3')
	for s in emolist:
		sound = AudioSegment.from_mp3(s)
		sound.export('wav/'+s.replace('mp3', 'wav'), format="wav")
