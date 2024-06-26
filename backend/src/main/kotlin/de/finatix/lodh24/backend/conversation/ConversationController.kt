package de.finatix.lodh24.backend.conversation

import de.finatix.lodh24.backend.conversation.db.Conversation
import org.springframework.web.bind.annotation.*
import java.util.*

@RestController
@RequestMapping("/api/conversations")
@CrossOrigin(origins = ["*"])
class ConversationController(private val conversationService: ConversationService) {

    @PostMapping
    fun startConversation(): ConversationResponse {
        val token = conversationService.startConversation()
        return ConversationResponse(token)
    }

    @PostMapping("/{conversationToken}/messages")
    fun sendMessage(
        @PathVariable conversationToken: UUID,
        @RequestBody message: UserMessage
    ): ConversationResponse {
        val response = conversationService.sendMessage(conversationToken, message.message)
        return ConversationResponse(conversationToken, response.text)
    }

    @GetMapping("/{conversationToken}")
    fun getConversation(@PathVariable conversationToken: UUID): Conversation {
        return conversationService.getConversation(conversationToken)
    }

    @GetMapping()
    fun getConversations(@RequestParam("tokens") tokens: List<UUID>): List<PastConversation> {
        val conversations = conversationService.getPastConversations(tokens)

        return conversations
    }
}

data class UserMessage(val message: String)

data class ConversationResponse(val conversationToken: UUID, val response: String? = null)
