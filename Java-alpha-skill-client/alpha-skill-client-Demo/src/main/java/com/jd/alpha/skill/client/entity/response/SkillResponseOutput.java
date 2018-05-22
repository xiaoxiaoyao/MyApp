package com.jd.alpha.skill.client.entity.response;

import com.jd.alpha.skill.client.constant.ResponseOutputTypeConstants;
import lombok.*;

/**
 * 类描述
 *
 * @author <b>作者：</b> D.Yang（cdyangyang18@jd.com） <br/>
 * <b>时间：</b> 2017/11/29 17:07 <br/>
 * <b>Copyright (c)</b> 2018 京东智能-版权所有 <br/>
 */
@Getter
@Setter
@ToString
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class SkillResponseOutput {

    @Builder.Default
    private String type = ResponseOutputTypeConstants.PLAIN_TEXT;

    private String text;

}
