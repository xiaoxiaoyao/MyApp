package com.jd.alpha.skill.client.entity.request;

import lombok.*;

import java.util.Map;

/**
 * Skill Request 意图信息
 *
 * @author <b>作者：</b> D.Yang（cdyangyang18@jd.com） <br/>
 * <b>时间：</b> 2017/11/29 15:48 <br/>
 * <b>Copyright (c)</b> 2018 京东智能-版权所有 <br/>
 */
@Getter
@Setter
@ToString
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class SkillRequestIntent {

    /**
     * 意图名称
     */
    private String name;

    /**
     * 意图确认类型
     */
    private String confirmResult;

    /**
     * 槽位信息
     */
    private Map<String, SkillRequestSlot> slots;

}
