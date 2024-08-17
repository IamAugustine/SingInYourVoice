import amphion
import bark
import soundfile as sf
import numpy as np
import torch 

# Function to encode the voice
def encode_voice(audio_path):
    # Load the audio file
    audio, sample_rate = sf.read(audio_path)
    # Encode the voice using Amphion
    encoder = amphion.VoiceEncoder()
    voice_embedding = encoder.encode(audio, sample_rate)
    return voice_embedding

# Function to synthesize speech
def synthesize_speech(text, voice_embedding):
    # Synthesize speech using the voice embedding
    synthesizer = amphion.SpeechSynthesizer()
    synthesized_audio = synthesizer.synthesize(text, voice_embedding)
    return synthesized_audio

# Function to convert the voice
def convert_voice(source_audio_path, target_audio_path):
    # Load the source and target audio files
    source_audio, source_sample_rate = sf.read(source_audio_path)
    target_audio, target_sample_rate = sf.read(target_audio_path)
    # Convert the voice using Bark
    converter = bark.VoiceConverter()
    converted_audio = converter.convert(source_audio, source_sample_rate, target_audio, target_sample_rate)
    return converted_audio

# Main function to handle the voice cloning process
def main():
    # Input audio file paths
    source_audio_path = 'source_audio.wav'
    target_audio_path = 'target_audio.wav'
    
    # Encode the source voice
    source_voice_embedding = encode_voice(source_audio_path)
    
    # Synthesize speech with the source voice
    text = "This is a test sentence."
    synthesized_audio = synthesize_speech(text, source_voice_embedding)
    
    # Save the synthesized audio
    sf.write('synthesized_audio.wav', synthesized_audio, 16000)
    
    # Convert the source voice to match the target voice
    converted_audio = convert_voice(source_audio_path, target_audio_path)
    
    # Save the converted audio
    sf.write('converted_audio.wav', converted_audio, 16000)
    
    print("Voice cloning completed successfully!")

if __name__ == "__main__":
    main()

