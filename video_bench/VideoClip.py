class VideoClip:
    def __init__(self, clip_id: str, resolution: str, frames: list):
        self.clip_id = clip_id
        self.resolution = resolution
        self.frames = frames

    def __len__(self) -> int:
        if self.frames is None:
            return 0
        else:
            return len(self.frames)
        
    def __str__(self):
        return f"🎬 [测试样本 {self.clip_id} 分辨率：{self.resolution}] | 包含帧数：{len(self)} 帧"


    def __add__(self, other):
        return self.frames + other.frames