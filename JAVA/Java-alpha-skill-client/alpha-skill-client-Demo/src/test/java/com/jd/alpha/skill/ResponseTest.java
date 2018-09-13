package com.jd.alpha.skill;

import com.jd.alpha.skill.client.constant.DirectiveTypeConstants;
import com.jd.alpha.skill.client.entity.response.SkillResponse;
import com.jd.alpha.skill.client.entity.response.SkillResponseDetails;
import com.jd.alpha.skill.client.entity.response.SkillResponseOutput;
import com.jd.alpha.skill.client.entity.response.directive.Directive;
import com.jd.alpha.skill.client.entity.response.directive.audio.AudioDirective;
import com.jd.alpha.skill.client.entity.response.directive.audio.AudioStream;
import org.junit.Test;

import java.util.ArrayList;
import java.util.List;

/**
 * 类描述
 *
 * @author <b>作者：</b> D.Yang（cdyangyang18@jd.com） <br/>
 * <b>时间：</b> 2018/1/8 10:46 <br/>
 * <b>Copyright (c)</b> 2018 京东智能-版权所有 <br/>
 */
public class ResponseTest {

    @Test
    public void testSkillResponse() {
        SkillResponse response = SkillResponse.builder()
                .skill("skillId")
                .shouldEndSession(false)
                .intent("query")
                .response(SkillResponseDetails.builder()
                        .output(SkillResponseOutput.builder()
                                .text("欢迎使用")
                                .build())
                        .build())
                .build();
        System.out.println(response);
    }

    @Test
    public void testAudioPlayerResponse() {
        List<Directive> directiveList = new ArrayList<>();
        directiveList.add(AudioDirective.builder()
                .type(DirectiveTypeConstants.AUDIO_PLAYER_PLAY)
                .audioStream(AudioStream.builder()
                        .name("睡前拉伸")
                        .url("http://static1.keepcdn.com/course/public/pre_bed_stretch.mp3")
                        .build())
                .build());

        SkillResponse response = SkillResponse.builder()
                .shouldEndSession(true)
                .response(SkillResponseDetails.builder()
                        .output(SkillResponseOutput.builder()
                                .text("即将为您播放睡前拉伸训练课程")
                                .build())
                        .build())
                .directives(directiveList)
                .build();

        System.out.println(response);
    }

}
