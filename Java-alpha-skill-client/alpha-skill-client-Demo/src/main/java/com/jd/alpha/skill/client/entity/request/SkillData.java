package com.jd.alpha.skill.client.entity.request;

import lombok.*;

/**
 * Skill Data
 *
 * @author <b>作者：</b> D.Yang（cdyangyang18@jd.com） <br/>
 * <b>时间：</b> 2017/12/29 15:31 <br/>
 * <b>Copyright (c)</b> 2017 京东智能-版权所有 <br/>
 */
@Getter
@Setter
@ToString
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class SkillData {

    /**
     * 版本号
     */
    @Builder.Default
    private String version = "1.0";

    /**
     * Session信息
     */
    private SkillSession session;

    /**
     * Request信息
     */
    private SkillRequest request;

}
