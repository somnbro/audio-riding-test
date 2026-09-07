import { useState } from "react";
import "./AudioInput.css";

function AudioInput(){
    const [audioFile, setAudioFile] = useState(null);


    const audioURL = audioFile ? URL.createObjectURL(audioFile) : null;

    if (!audioFile){
        return (
            <div className="audioInputBlock">
                <label htmlFor="audio-upload" id="audio-upload-text">
                    Input audio here
                </label>
                <input 
                    id= "audio-upload" 
                    type="file" 
                    accept="audio/*" 
                    onChange={(event) => setAudioFile(event.target.files[0])}
                />
            </div>
        );
    }
    else {
        return (
            <div className="audioInputBlock">
                <div className="btnHolder">
                    <p>{audioFile?.name}</p>
                    <audio controls src={audioURL}></audio>
                    <button onClick={()=>setAudioFile(null)}> X </button>
                </div>
                
            </div>
        );
    }
        
}

export default AudioInput;