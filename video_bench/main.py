from VideoClip import VideoClip

if __name__ == "__main__":
    # 实例化两个视频片段样本
    clip_A = VideoClip("V-001", "1080p", ["A_frame1.jpg", "A_frame2.jpg", "A_frame3.jpg"])
    clip_B = VideoClip("V-002", "1080p", ["B_frame1.jpg", "B_frame2.jpg"])

    # 测试 __len__ (大模型读取帧数)
    print("--- 样本帧数检测 ---")
    print(f"片段 A 共有 {len(clip_A)} 帧")

    # 测试 __str__ (控制台打印状态)
    print("\n--- 评测控制台输出 ---")
    print(clip_A)
    print(clip_B)

    # 测试 __add__ （长视频上下文拼接）
    print("\n--- 上下文拼接测试 ---")
    long_context_frames = clip_A + clip_B
    print(f"合并后的输入序列：{long_context_frames}")