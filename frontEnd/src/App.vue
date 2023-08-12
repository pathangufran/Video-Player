<template>
  <div id="app">
    <h1 class="title">Video Subtitles</h1>
    <div v-for="(video, index) in videos" :key="index" class="video-container">
      <div class="video-wrapper">
        <video :ref="'videoPlayer-' + video.id" :controls="true" class="video-player" width="480" height="270" @timeupdate="syncSubtitles(video)">
          <source :src="video.videoUrl" type="video/mp4" />
          <track v-for="(subtitle, subtitleIndex) in video.subtitles" :key="subtitleIndex" :src="subtitleUrl(subtitle)" kind="subtitles" srclang="en" default />
        </video>
        <div class="subtitle-form">
          <input type="text" class="subtitle-input" placeholder="Enter subtitle text" v-model="subtitleText">
          <input type="number" step="0.1" class="timestamp-input" placeholder="Enter timestamp" v-model="timestamp">
          <button @click="addSubtitle(video, index)" class="add-button">Add Subtitle</button>
        </div>
        <div class="subtitles">
          <div v-for="subtitle in video.subtitles" :key="subtitle.id" class="subtitle">
            {{ subtitle.subtitle_text }} ({{ subtitle.timestamp }})
          </div>
        </div>
      </div>
    </div>
    <div class="upload-container">
      <label class="upload-button">
        Upload Video
        <input type="file" @change="uploadVideo" class="upload-input">
      </label>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      videos: [],
      subtitleText: '',
      timestamp: 0,
    };
  },
  methods: {
    async uploadVideo(event) {
      const formData = new FormData();
      formData.append('video', event.target.files[0]);

      try {
        await axios.post('http://localhost:8000/api/videos/', formData);
        this.fetchVideos();
        alert('Video uploaded successfully');
      } catch (error) {
        console.error(error);
        alert('Error uploading video');
      }
    },
    async fetchVideos() {
      try {
        const response = await axios.get('http://localhost:8000/api/videos/');
        this.videos = response.data.map(video => ({
          id: video.id,
          videoUrl: new URL(video.video, 'http://localhost:8000').toString(),
          subtitles: [],
        }));
        this.fetchSubtitles();
      } catch (error) {
        console.error(error);
      }
    },
    async addSubtitle(video, index) {
      try {
        await axios.post('http://localhost:8000/api/subtitles/', {
          video: video.id,
          timestamp: parseFloat(this.timestamp),
          subtitle_text: this.subtitleText,
        });
        this.fetchSubtitles(index);
        this.subtitleText = '';
        this.timestamp = 0;
      } catch (error) {
        console.error(error);
      }
    },
    async fetchSubtitles(index) {
      try {
        if (index >= 0 && index < this.videos.length) {
          const video = this.videos[index];
          const response = await axios.get(`http://localhost:8000/api/subtitles/?video=${video.id}`);
          video.subtitles = response.data;
        }
      } catch (error) {
        console.error(error);
      }
    },
    syncSubtitles(video) {
      const videoElement = this.$refs[`videoPlayer-${video.id}`][0];
      const currentTime = videoElement.currentTime;
      const subtitles = video.subtitles;

      for (let i = 0; i < subtitles.length; i++) {
        const subtitle = subtitles[i];
        if (currentTime >= subtitle.timestamp) {
          videoElement.nextElementSibling.innerText = subtitle.subtitle_text;
        } else {
          videoElement.nextElementSibling.innerText = '';
          break;
        }
      }
    },
    subtitleUrl(subtitle) {
      return `http://localhost:8000${subtitle.subtitle_file}`;
    },
  },
  mounted() {
    this.fetchVideos();
  },
};
</script>

<style scoped>
.title {
  text-align: center;
  margin-bottom: 20px;
  font-size: 24px;
}

.video-container {
  margin-bottom: 30px;
}

.video-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.video-player {
  max-width: 100%;
  height: auto;
  border:none;
  border-radius: 10px;
}

.subtitle-form {
  margin-top: 10px;
  display: flex;
  align-items: center;
}

.subtitle-input, .timestamp-input {
  padding: 5px;
  margin-right: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.add-button {
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 5px 10px;
  cursor: pointer;
}

.subtitles {
  margin-top: 10px;
}

.subtitle {
  margin-top: 5px;
  font-size: 14px;
}

.upload-container {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

.upload-button {
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 8px 16px;
  cursor: pointer;
  display: inline-block;
  text-align: center;
  font-size: 16px;
}

.upload-input {
  display: none;
}
</style>

