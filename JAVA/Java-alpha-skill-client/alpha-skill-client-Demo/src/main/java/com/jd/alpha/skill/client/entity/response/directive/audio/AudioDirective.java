package com.jd.alpha.skill.client.entity.response.directive.audio;

import com.jd.alpha.skill.client.entity.response.directive.Directive;
import lombok.*;

/**
 * 类描述
 *
 * @author <b>作者：</b> D.Yang（cdyangyang18@jd.com） <br/>
 * <b>时间：</b> 2017/11/29 17:21 <br/>
 * <b>Copyright (c)</b> 2018 京东智能-版权所有 <br/>
 */
@Getter
@Setter
@ToString
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class AudioDirective extends Directive {

    private String type;

    private String name;

    private String playBehavior;

    private AudioStream audioStream;

}