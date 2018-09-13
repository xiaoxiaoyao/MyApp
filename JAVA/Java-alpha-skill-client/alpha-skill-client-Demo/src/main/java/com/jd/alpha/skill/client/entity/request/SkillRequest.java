package com.jd.alpha.skill.client.entity.request;

import lombok.*;

/**
 * Skill Request
 *
 * @author <b>作者：</b> D.Yang（cdyangyang18@jd.com） <br/>
 * <b>时间：</b> 2017/11/29 15:40 <br/>
 * <b>Copyright (c)</b> 2018 京东智能-版权所有 <br/>
 */
@Getter
@Setter
@ToString
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class SkillRequest {

    /**
     * 请求编号
     */
    private String requestId;

    /**
     * 请求类型
     */
    private String type;

    /**
     * 请求时间戳
     */
    private Long timestamp;

    /**
     * 对话状态
     */
    private String dialogState;

    /**
     * 意图信息
     */
    private SkillRequestIntent intent;

}