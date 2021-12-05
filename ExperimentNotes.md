# Automatic Transcription for Video Conferencing Platforms

This document describes how to set up the local environment to conduct experiments for the IoT **ATS** project. For information on the tool used to play and convert audio files, refer to the [local readme](./README.md).

Note: Due to the limitations of the video conferencing platforms analyzed in this experiment, these experiments are designed and utilize tools only available to Windows and Mac operating systems.

Note: Due to the nature of the experiment:
 - **Virtual output** must be wired to the video conferencing platfrom **microphone input** for all platforms. 
 - **Virtual input** should be routed to the video conferencing platform **speaker output**.

## Documented Platforms
- Zoom
- BlueJeans
- Cisco Webex
- Google Meet

### Zoom

Download link: https://zoom.us/download

Automatic Transcript Instructions: https://support.zoom.us/hc/en-us/articles/115004794983-Audio-transcription-for-cloud-recordings

Instructions for local setup:
- Download the application
- Open the application and sign into an account
- On the **Home** screen, select *New Meeting*
- Join the call with computer audio
- After joining the call, navigate to the microphone icon in the bottom left corner of the window
- Click the `^` symbol and select the appropriate Virtual Cable input and outputs
- Click the **Live Transcription** button at the bottom of the window and select **Enable Autotranscription**
- In the bottom portion of the screen, select **Record** and elect to store it in the cloud
- To view the transcript (and download it locally *without* the cloud), select the `^` character on the **Live Transcription** button and select **View Full Transcript**

### BlueJeans

Note:: For prolonged experiments, a second account must be attending the meeting; otherwise the meeting window will close after a set amount of time, regardless of whether or not there is visual or audio input.

Download link: https://www.bluejeans.com/downloads

Automatic Transcript Instructions: https://support.bluejeans.com/s/article/Smart-Meetings-Highlights-and-Transcription

Instructions for local setup:
- Download the application
- Open the application and sign into an account
- On the bottom of the screen, assign the appropriate Virtual Cable input and output
- Once the audio has been set up, click **Start** in the upper left hand corner of the screen
- In the top left corner of the meeting window, select **Start Rec & Highlights** to start recording and transcription to the cloud

### Cisco Webex

Note:: For prolonged experiments, a second account must be attending the meeting; otherwise the meeting window will close after a set amount of time, regardless of whether or not there is visual or audio input.

Download link: https://www.webex.com/downloads.html

Automatic Transcript Instructions: https://help.webex.com/en-US/article/uq5009/Enable-Recording-Transcripts-in-Cisco-Webex-Meetings-and-Webex-Events-

Instructions for local setup:
- Download the application
- Open the application and sign into an account
- On the left sidebar, click the **Meetings** icon (looks a bit like a calendar)
- In the top right hand corner of the screen, click the **Start** button in the upper right hand corner of the window
- In the windows that appears, select **Test speaker and microphone** in the bottom right corner of the screen
- Set the apprpriate Virtual Cable input and output channels
- Click **Start Meeting** on the bottom portion of the screen
- In the bottom right corner of the meeting window, select the ellipsis icon (`...`) and select **Captions and Highlights**
- Click **Record** to start recording to make transcription available in cloud after the meeting

### Google Meet

Note:: Google Meet requires an additional tool to capture automated captions and a Google account to store the resulting files. Simply add the [Scribbl Google Meets Transcript](https://chrome.google.com/webstore/detail/google-meet-transcripts-b/kmjmlilenakedodldceipdnmmnfkahni?hl=en-US) tool to your Chrome instance as an extension before setting up the experiment. 

Instructions for local setup:
- Open Chrome with your Google Account signed in
- Navigate to the Google Meet application
- Start an instant meeting
- Click **New Meeting**
- Click **Start Instant Meeting**
- In the meeting window, click the vertical ellpsis at the bottom of the screen and select **Settings**
- In the windows that appears, set the appropriate Virtual Cable input and output channels
- To start autocaptioning, select the **CC** button on the toolbar on the *right* side of the screen
- The resulting transcript will be openned in the browser after the meeting and will be available in the Google Drive of the account hosting the meeting

## Additional Tools
- Ffmpeg
- VB Virtual Audio Cable

### Ffmpeg

**MacOS:**

Mac users should refer to [this documentation](http://trac.ffmpeg.org/wiki/CompilationGuide/macOS#:~:text=There%20are%20a%20few%20ways,%E2%80%8BMacPorts%20to%20install%20ffmpeg%20.&text=See%20the%20Homebrew%20section%20below%20for%20more%20info.) for install instructions. Ffmpeg will then be available from your command line.

**Windows OS**

Download link: https://www.ffmpeg.org/

Instructions:
- Download the file from the source site
- Unzip the contents of the file and navigate to the resulting directory
- Take the `ffmpeg.exe` file from the directory and place it into the local directory (same directory as this Markdown file)

Note: Advanced users can add the absolute path to the directory containing `ffmpeg.exe` to their systems **Environment Variables** to make the command available at the command line.

## VB Virtual Audio Cable

Note:: Usage of the Virtual Audio Cable inputs and outputs should be configured for each individual video conferencing platform. Refer to individual instructions on the video conferencing platform to determine where these values are set.

Download link: https://vb-audio.com/Cable/index.htm

Instructions:
- Download the file for the appropriate operating system
- Unzip the folder and navigate to the resulting directory
- Start the `VBCable_Setup` file and use the wizard to download the virtual cable on your machine