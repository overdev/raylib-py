from library import rl as _rl
from structures import *
from ctypes import byref


__all__ = [
    'init_audio_device',
    'close_audio_device',
    'is_audio_device_ready',
    'set_master_volume',
    'load_wave',
    'load_wave_ex',
    'load_sound',
    'load_sound_from_wave',
    'update_sound',
    'unload_wave',
    'unload_sound',
    'play_sound',
    'pause_sound',
    'resume_sound',
    'stop_sound',
    'is_sound_playing',
    'set_sound_volume',
    'set_sound_pitch',
    'wave_format',
    'wave_copy',
    'wave_crop',
    'get_wave_data',
    'load_music_stream',
    'unload_music_stream',
    'play_music_stream',
    'update_music_stream',
    'stop_music_stream',
    'pause_music_stream',
    'resume_music_stream',
    'is_music_playing',
    'set_music_volume',
    'set_music_pitch',
    'set_music_loop_count',
    'get_music_time_length',
    'get_music_time_played',
    'init_audio_stream',
    'update_audio_stream',
    'close_audio_stream',
    'is_audio_buffer_processed',
    'play_audio_stream',
    'pause_audio_stream',
    'resume_audio_stream',
    'is_audio_stream_playing',
    'stop_audio_stream',
    'set_audio_stream_volume',
    'set_audio_stream_pitch',
]

_NOARGS = []


# -----------------------------------------------------------------------------------
# Audio Loading and Playing Functions (Module: audio)
# -----------------------------------------------------------------------------------

# Audio device management functions
_rl.InitAudioDevice.argtypes = _NOARGS
_rl.InitAudioDevice.restype = None
def init_audio_device() -> None:
    '''Initialize audio device and context'''
    return _rl.InitAudioDevice()


_rl.CloseAudioDevice.argtypes = _NOARGS
_rl.CloseAudioDevice.restype = None
def close_audio_device() -> None:
    '''Close the audio device and context'''
    return _rl.CloseAudioDevice()


_rl.IsAudioDeviceReady.argtypes = _NOARGS
_rl.IsAudioDeviceReady.restype = Bool
def is_audio_device_ready():
    '''Check if audio device has been initialized successfully'''
    return _rl.IsAudioDeviceReady()


_rl.SetMasterVolume.argtypes = [Float]
_rl.SetMasterVolume.restype = None
def set_master_volume(volume: float) -> None:
    '''Set master volume (listener)'''
    return _rl.SetMasterVolume(volume)


# Wave/Sound loading/unloading functions
_rl.LoadWave.argtypes = [CharPtr]
_rl.LoadWave.restype = Wave
def load_wave(fileName: CharPtr) -> Wave:
    '''Load wave data from file'''
    return _rl.LoadWave(fileName)


_rl.LoadWaveEx.argtypes = [VoidPtr, Int, Int, Int, Int]
_rl.LoadWaveEx.restype = Wave
def load_wave_ex(data: VoidPtr, sampleCount: int, sampleRate: int, sampleSize: int, channels: int) -> Wave:
    '''Load wave data from raw array data'''
    return _rl.LoadWaveEx(data, sampleCount, sampleRate, sampleSize, channels)


_rl.LoadSound.argtypes = [CharPtr]
_rl.LoadSound.restype = Sound
def load_sound(fileName: CharPtr) -> Sound:
    '''Load sound from file'''
    return _rl.LoadSound(fileName)


_rl.LoadSoundFromWave.argtypes = [Wave]
_rl.LoadSoundFromWave.restype = Sound
def load_sound_from_wave(wave: Wave) -> Sound:
    '''Load sound from wave data'''
    return _rl.LoadSoundFromWave(wave)


_rl.UpdateSound.argtypes = [Sound, VoidPtr, Int]
_rl.UpdateSound.restype = None
def update_sound(sound: Sound, data: VoidPtr, samplesCount: int) -> None:
    '''Update sound buffer with new data'''
    return _rl.UpdateSound(sound, data, samplesCount)


_rl.UnloadWave.argtypes = [Wave]
_rl.UnloadWave.restype = None
def unload_wave(wave: Wave) -> None:
    '''Unload wave data'''
    return _rl.UnloadWave(wave)


_rl.UnloadSound.argtypes = [Sound]
_rl.UnloadSound.restype = None
def unload_sound(sound: Sound) -> None:
    '''Unload sound'''
    return _rl.UnloadSound(sound)


# Wave/Sound management functions
_rl.PlaySound.argtypes = [Sound]
_rl.PlaySound.restype = None
def play_sound(sound: Sound) -> None:
    '''Play a sound'''
    return _rl.PlaySound(sound)


_rl.PauseSound.argtypes = [Sound]
_rl.PauseSound.restype = None
def pause_sound(sound: Sound) -> None:
    '''Pause a sound'''
    return _rl.PauseSound(sound)


_rl.ResumeSound.argtypes = [Sound]
_rl.ResumeSound.restype = None
def resume_sound(sound: Sound) -> None:
    '''Resume a paused sound'''
    return _rl.ResumeSound(sound)


_rl.StopSound.argtypes = [Sound]
_rl.StopSound.restype = None
def stop_sound(sound: Sound) -> None:
    '''Stop playing a sound'''
    return _rl.StopSound(sound)


_rl.IsSoundPlaying.argtypes = [Sound]
_rl.IsSoundPlaying.restype = Bool
def is_sound_playing(sound: Sound) -> bool:
    '''Check if a sound is currently playing'''
    return _rl.IsSoundPlaying(sound)


_rl.SetSoundVolume.argtypes = [Sound, Float]
_rl.SetSoundVolume.restype = None
def set_sound_volume(sound: Sound, volume: float) -> None:
    '''Set volume for a sound (1.0 is max level)'''
    return _rl.SetSoundVolume(sound, volume)


_rl.SetSoundPitch.argtypes = [Sound, Float]
_rl.SetSoundPitch.restype = None
def set_sound_pitch(sound: Sound, pitch: float) -> None:
    '''Set pitch for a sound (1.0 is base level)'''
    return _rl.SetSoundPitch(sound, pitch)


_rl.WaveFormat.argtypes = [WavePtr, Int, Int, Int]
_rl.WaveFormat.restype = None
def wave_format(wave: WavePtr, sampleRate: int, sampleSize: int, channels: int) -> None:
    '''Convert wave data to desired format'''
    return _rl.WaveFormat(wave, sampleRate, sampleSize, channels)


_rl.WaveCopy.argtypes = [Wave]
_rl.WaveCopy.restype = Wave
def wave_copy(wave: Wave) -> Wave:
    '''Copy a wave to a new wave'''
    return _rl.WaveCopy(wave)


_rl.WaveCrop.argtypes = [WavePtr, Int, Int]
_rl.WaveCrop.restype = None
def wave_crop(wave: WavePtr, initSample: int, finalSample: int) -> None:
    '''Crop a wave to defined samples range'''
    return _rl.WaveCrop(wave, initSample, finalSample)


_rl.GetWaveData.argtypes = [Wave]
_rl.GetWaveData.restype = FloatPtr
def get_wave_data(wave: Wave) -> FloatPtr:
    '''Get samples data from wave as a floats array'''
    return _rl.GetWaveData(wave)


# Music management functions
_rl.LoadMusicStream.argtypes = [CharPtr]
_rl.LoadMusicStream.restype = Music
def load_music_stream(fileName: CharPtr) -> Music:
    '''Load music stream from file'''
    return _rl.LoadMusicStream(fileName)


_rl.UnloadMusicStream.argtypes = [Music]
_rl.UnloadMusicStream.restype = None
def unload_music_stream(music: Music) -> None:
    '''Unload music stream'''
    return _rl.UnloadMusicStream(music)


_rl.PlayMusicStream.argtypes = [Music]
_rl.PlayMusicStream.restype = None
def play_music_stream(music: Music) -> None:
    '''Start music playing'''
    return _rl.PlayMusicStream(music)


_rl.UpdateMusicStream.argtypes = [Music]
_rl.UpdateMusicStream.restype = None
def update_music_stream(music: Music) -> None:
    '''Updates buffers for music streaming'''
    return _rl.UpdateMusicStream(music)


_rl.StopMusicStream.argtypes = [Music]
_rl.StopMusicStream.restype = None
def stop_music_stream(music: Music) -> None:
    '''Stop music playing'''
    return _rl.StopMusicStream(music)


_rl.PauseMusicStream.argtypes = [Music]
_rl.PauseMusicStream.restype = None
def pause_music_stream(music: Music) -> None:
    '''Pause music playing'''
    return _rl.PauseMusicStream(music)


_rl.ResumeMusicStream.argtypes = [Music]
_rl.ResumeMusicStream.restype = None
def resume_music_stream(music: Music) -> None:
    '''Resume playing paused music'''
    return _rl.ResumeMusicStream(music)


_rl.IsMusicPlaying.argtypes = [Music]
_rl.IsMusicPlaying.restype = Bool
def is_music_playing(music: Music):
    '''Check if music is playing'''
    return _rl.IsMusicPlaying(music)


_rl.SetMusicVolume.argtypes = [Music, Float]
_rl.SetMusicVolume.restype = None
def set_music_volume(music: Music, volume: float) -> None:
    '''Set volume for music (1.0 is max level)'''
    return _rl.SetMusicVolume(music, volume)


_rl.SetMusicPitch.argtypes = [Music, Float]
_rl.SetMusicPitch.restype = None
def set_music_pitch(music: Music, pitch: float) -> None:
    '''Set pitch for a music (1.0 is base level)'''
    return _rl.SetMusicPitch(music, pitch)


_rl.SetMusicLoopCount.argtypes = [Music, Int]
_rl.SetMusicLoopCount.restype = None
def set_music_loop_count(music: Music, count: int) -> None:
    '''Set music loop count (loop repeats)'''
    return _rl.SetMusicLoopCount(music, count)


_rl.GetMusicTimeLength.argtypes = [Music]
_rl.GetMusicTimeLength.restype = Float
def get_music_time_length(music: Music) -> float:
    '''Get music time length (in seconds)'''
    return _rl.GetMusicTimeLength(music)


_rl.GetMusicTimePlayed.argtypes = [Music]
_rl.GetMusicTimePlayed.restype = Float
def get_music_time_played(music: Music) -> float:
    '''Get current music time played (in seconds)'''
    return _rl.GetMusicTimePlayed(music)


# AudioStream management functions
_rl.InitAudioStream.argtypes = [UInt, UInt, UInt]
_rl.InitAudioStream.restype = AudioStream
def init_audio_stream(sampleRate: int, sampleSize: int, channels: int) -> AudioStream:
    '''Init audio stream (to stream raw audio pcm data)'''
    return _rl.InitAudioStream(sampleRate, sampleSize, channels)


_rl.UpdateAudioStream.argtypes = [AudioStream, VoidPtr, Int]
_rl.UpdateAudioStream.restype = None
def update_audio_stream(stream: AudioStream, data: VoidPtr, samplesCount: int) -> None:
    '''Update audio stream buffers with data'''
    return _rl.UpdateAudioStream(stream, data, samplesCount)


_rl.CloseAudioStream.argtypes = [AudioStream]
_rl.CloseAudioStream.restype = None
def close_audio_stream(stream: AudioStream) -> None:
    '''Close audio stream and free memory'''
    return _rl.CloseAudioStream(stream)


_rl.IsAudioBufferProcessed.argtypes = [AudioStream]
_rl.IsAudioBufferProcessed.restype = Bool
def is_audio_buffer_processed(stream: AudioStream) -> bool:
    '''Check if any audio stream buffers requires refill'''
    return _rl.IsAudioBufferProcessed(stream)


_rl.PlayAudioStream.argtypes = [AudioStream]
_rl.PlayAudioStream.restype = None
def play_audio_stream(stream: AudioStream) -> None:
    '''Play audio stream'''
    return _rl.PlayAudioStream(stream)


_rl.PauseAudioStream.argtypes = [AudioStream]
_rl.PauseAudioStream.restype = None
def pause_audio_stream(stream: AudioStream) -> None:
    '''Pause audio stream'''
    return _rl.PauseAudioStream(stream)


_rl.ResumeAudioStream.argtypes = [AudioStream]
_rl.ResumeAudioStream.restype = None
def resume_audio_stream(stream: AudioStream) -> None:
    '''Resume audio stream'''
    return _rl.ResumeAudioStream(stream)


_rl.IsAudioStreamPlaying.argtypes = [AudioStream]
_rl.IsAudioStreamPlaying.restype = Bool
def is_audio_stream_playing(stream: AudioStream) -> bool:
    '''Check if audio stream is playing'''
    return _rl.IsAudioStreamPlaying(stream)


_rl.StopAudioStream.argtypes = [AudioStream]
_rl.StopAudioStream.restype = None
def stop_audio_stream(stream: AudioStream) -> None:
    '''Stop audio stream'''
    return _rl.StopAudioStream(stream)


_rl.SetAudioStreamVolume.argtypes = [AudioStream, Float]
_rl.SetAudioStreamVolume.restype = None
def set_audio_stream_volume(stream: AudioStream, volume: float) -> None:
    '''Set volume for audio stream (1.0 is max level)'''
    return _rl.SetAudioStreamVolume(stream, volume)


_rl.SetAudioStreamPitch.argtypes = [AudioStream, Float]
_rl.SetAudioStreamPitch.restype = None
def set_audio_stream_pitch(stream: AudioStream, pitch: float) -> None:
    '''Set pitch for audio stream (1.0 is base level)'''
    return _rl.SetAudioStreamPitch(stream, pitch)
