package com.jd.alpha.skill.client.entity.response;

import com.jd.alpha.skill.client.entity.response.directive.Directive;
import lombok.*;

import java.util.List;
import java.util.Map;

/**
 * 类描述
 *
 * @author <b>作者：</b> D.Yang（cdyangyang18@jd.com） <br/>
 * <b>时间：</b> 2017/11/29 17:01 <br/>
 * <b>Copyright (c)</b> 2018 京东智能-版权所有 <br/>
 */
@Getter
@Setter
@ToString
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class SkillResponse {

    @Builder.Default
    private String version = "1.0";

    private String skill;

    private String intent;

    @Builder.Default
    private boolean shouldEndSession = false;

    private Map<String, Object> contexts;

    private SkillResponseDetails response;

    private List<Directive> directives;

}
