from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from gtts import gTTS
import os

class VoiceChangerApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        self.title_label = Label(text="Voice Changer Studio", font_size='24sp', size_hint=(1, 0.2))
        layout.add_widget(self.title_label)
        
        self.text_input = TextInput(text="Hello! Welcome to Voice Changer Studio.", multiline=True, size_hint=(1, 0.4))
        layout.add_widget(self.text_input)
        
        self.status_label = Label(text="Status: Ready", size_hint=(1, 0.15))
        layout.add_widget(self.status_label)
        
        btn = Button(text="Generate Audio", size_hint=(1, 0.25), background_color=(0.2, 0.6, 1, 1))
        btn.bind(on_press=self.generate_audio)
        layout.add_widget(btn)
        
        return layout

    def generate_audio(self, instance):
        try:
            text = self.text_input.text
            if not text.strip():
                self.status_label.text = "Status: Please enter some text!"
                return
            
            tts = gTTS(text=text, lang='en')
            output_file = "voice_output.mp3"
            tts.save(output_file)
            self.status_label.text = f"Status: Saved to {output_file}!"
        except Exception as e:
            self.status_label.text = f"Error: {str(e)}"

if __name__ == "__main__":
    VoiceChangerApp().run()
