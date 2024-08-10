from pydub import AudioSegment

# Memuat file audio
audio = AudioSegment.from_file('cocomelon.mp3')

# Menyimpan file audio
audio.export('result.mp3', format='mp3')

#### Pemotongan

clipped_audio = audio[:10000]  # Mendapatkan 10 detik pertama
clipped_audio.export('clipped_result.mp3', format='mp3')

#### Penggabungan

combined_audio = audio + clipped_audio
combined_audio.export('combined_result.mp3', format='mp3')

#### Konversi Format

audio.export('result.wav', format='wav')

#### Pengaturan Volume

louder_audio = audio + 10  # Meningkatkan volume sebesar 10dB
louder_audio.export('louder_result.mp3', format='mp3')

